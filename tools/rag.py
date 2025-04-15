import os
import bs4
from langchain_community.document_loaders import UnstructuredPDFLoader, DirectoryLoader ,WebBaseLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
GROQ_API_KEY = "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"

os.environ["GROQ_API_KEY"] = GROQ_API_KEY

loader = WebBaseLoader(
    web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer(
            class_=("post-content", "post-title", "post-header")
        )
    ),
)
documents = loader.load()

text_splitter = CharacterTextSplitter(
    chunk_size=2000,
    chunk_overlap=500
)

text_chunks = text_splitter.split_documents(documents)

persist_directory = "doc_db"
embedding = HuggingFaceEmbeddings()
vectorstore = Chroma.from_documents(
    documents=text_chunks,
    embedding=embedding,
    persist_directory=persist_directory
)


retriever = vectorstore.as_retriever()
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)
query = "What is Task Decomposition?"
response = qa_chain.invoke({"query":query})

print(response['result'])