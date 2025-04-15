# from langchain_unstructured import UnstructuredLoader

# file_paths = [
#     "/home/silkadmin/Desktop/tools_langchain/data/pdf/income_tax.txt"
# ]


# loader = UnstructuredLoader(file_paths)


# docs = loader.load()

# docs[0]


# from unstructured.partition.auto import partition
# elements = partition("/home/silkadmin/Desktop/tools_langchain/data/pdf/manual.pdf")

# print(elements)

from langchain_unstructured import UnstructuredLoader
from unstructured.cleaners.core import clean_extra_whitespace

loader = UnstructuredLoader(
    "/home/silkadmin/Desktop/tools_langchain/data/pdf/MoRTH Circular - Design and General Features for bridge structures.pdf",
    post_processors=[clean_extra_whitespace],
)

docs = loader.load()

docs[5:10]