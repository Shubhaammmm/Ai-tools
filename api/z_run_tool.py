import importlib
import os
from tools.gemini_ocr import prep_image
from tools.gemini_ocr import extract_text_from_image
#from langchain.tools import BaseTool
from tools.texttospeech import ElevenLabsText2SpeechTool
from tools.g_serper import search_g
#from tools.wikipedia import Wikipedia
from tools.duck import DuckDuckGo
from tools.alpha import AlphaVantageTool
from tools.exa_search import ExaSearchTool
#from tools.tavily import search_tavily
#from tools.nasa import search_nasa
#from tools.linkup_search_tool import search_link
from tools.grad import GradioTool
#from tools.shell_tool import CustomShellTool
from tools.dataframe import DataFrameTool
#from tools.pubmed_search import Pubmed
#from tools.repl import execute_python_code
from tools.image_captions import get_image_explanation
#from tools.smart_scraper import scrape_website
#from tools.markdown import markdownify_website
from tools.document_ocr import perform_upstage_ocr
from tools.webscraper import scrape_all_content
from tools.finance_news import get_finance_news
#from tools.search_books import search_books
from tools.extractor import read_document
#from tools.sentiment_analysis import sentiment
from tools.generate_image import generate_image
from tools.website_screenshot import take_screenshot
#from tools.ocr import extract_text_from_scanned_pdf


def list_available_tools():
    """
    List all tool names present in the 'tools' folder by returning their filenames without the .py extension.

    Returns:
        list: A list of tool names (filenames without the .py extension).
    """
    tools_dir = "tools"  # Folder where all tool modules are stored
    tool_names = []

    try:
        # Check if tools directory exists
        if not os.path.exists(tools_dir):
            raise FileNotFoundError(f"Directory '{tools_dir}' not found.")

        # Iterate through all files in the directory
        for file in os.listdir(tools_dir):
            if file.endswith(".py") and not file.startswith("__"):  # Ignore __init__.py and hidden files
                tool_name = file[:-3]  # Remove the '.py' extension
                tool_names.append(tool_name)

    except Exception as e:
        print(f"Error accessing tools directory: {e}")

    return tool_names


def run_tool(command):
    tool_name = command.get("tool", "").lower()
    data = command.get("data", {})
    message = data.get("message")
    params = data.get("params", {})
    operation = data.get("operation")


    try:
        print(f"Received command: {command}")  
        print(f"Tool name: {tool_name}")
        print(f"Command data: {data}")

        # if tool_name == "wikipedia":
        #     wikipedia_tool = Wikipedia()  # Create the tool instance
        #     response = wikipedia_tool.run(message)  # Call the run method of the tool
        #     return response
        
        if tool_name == "gemini_ocr":
            sample_file = params.get("url")
            prompt=data.get("message")
            path=prep_image(sample_file)
            response=extract_text_from_image(path,prompt)
            return response
        elif tool_name == "duckduckgo":
            # Instantiate the DuckDuckGo tool and use the search_with_retry method
            duckduckgo_tool = DuckDuckGo(retries=3, delay=5)  # Create the DuckDuckGo instance
            response = duckduckgo_tool.search_with_retry(message)  # Perform the search with retry logic
            return response
        
        # elif tool_name == "ocr":
        #     url=params.get("url")
        #     text=extract_text_from_scanned_pdf(url)
        #     return text
        
        elif tool_name == "elevenlabs":
            message = data.get("message")
            if not message:
                return {"status": "error", "message": "Message is required for text-to-speech"}
            tts_tool = ElevenLabsText2SpeechTool()
            speech_file = tts_tool.run(message)  # Using the `run` method instead of `run_tool`
            tts_tool.stream(speech_file)  # Stream the audio
            return {"status": "success", "message": "Speech generated and played successfully."}
        
        elif tool_name == "alpha_vantage":
            av_tool = AlphaVantageTool()
            return av_tool._run(data.get("command"), data.get("params"))
        
        
        elif tool_name == 'googleserper':
            query=data.get("message")
            if not query:
                return {"status": "error", "message": "Message is required for text-to-speech"}
            response=search_g(query)
            return response
        # elif tool_name == "tavily":
        #     query=data.get("message")
        #     if not query:
        #         return {"status": "error", "message": "Message is required for text-to-speech"}
        #     response = search_tavily(query)
        #     return response
        elif tool_name == "list_tools":
            tools = list_available_tools()
            return {"status": "success", "tools": tools}
        
        # elif tool_name == "shell_tool":
        #     shell_tool = CustomShellTool()
        #     return shell_tool._run(data.get("command"), data.get("params"))
        
        elif tool_name == "exa_search":
            if not message or not operation:
                return {"status": "error", "message": "Missing 'message' or 'operation' parameter in 'data'."}
            return ExaSearchTool.execute(message, operation)
        
        elif tool_name == "gradio_tool":
            if not message or not operation:
                return {"status": "error", "message": "Missing 'message' or 'operation' parameter in 'data'."}
            return GradioTool.execute(message, operation)
        # # elif tool_name == "linkup_search":
        # #     query=data.get("message")
        # #     if not query:
        # #         return {"status": "error", "message": "Message is required for linkup_search"}
        # #     response = search_link(query)
        #     return response
        # elif tool_name == "nasa_search":
        #     query=data.get("message")
        #     if not query:
        #         return {"status": "error", "message": "Message is required for nasa_search"}
        #     response=search_nasa(query)
        #     return response
        elif tool_name == "data_frame":
                csv_url = params.get("csv_url")
                if not csv_url:
                    return {"status": "error", "message": "Missing 'csv_url' in parameters."}
                return DataFrameTool.query_dataframe(message, csv_url)
        # elif tool_name == "pub_med":
        #     query=data.get("message")
        #     if not query:
        #         return {"status": "error", "message": "Message is required for pubmed"}
        #     response=Pubmed(query)
        #     return response
        # elif tool_name == "python_repl":
        #     query=data.get("message")
        #     if not query:
        #         return {"status": "error", "message": "Message is required for Python repl"}
        #     response=execute_python_code(query)
        #     return response
        
        elif tool_name == "image_caption":
            url = params.get("url")
            query = data.get("message")

            if not url:
                return {"status": "error", "message": "Image path is required for image_caption"}
            if not query:
                return {"status": "error", "message": "Message is required for image_caption"}

            
            response = get_image_explanation(url, query)
            return {"status": "success", "data": response}
        # elif tool_name == "scrape_website":
        #     url=params.get("url")
        #     query=data.get("message")
        #     if not url:
        #         return {"status": "error", "message": "Image path is required for image_caption"}
        #     if not query:
        #         return {"status": "error", "message": "Message is required for image_caption"}

           
        #     response = scrape_website(url, query)
        #     return {"status": "success", "data": response}
        # elif tool_name == "markdown":
        #     url=params.get("url")
        #     if not url:
        #         return {"status": "error", "message": "Image path is required for image_caption"}
        #     response = markdownify_website(url)
        #     return {"status": "success", "data": response}
        
        elif tool_name =="document_ocr":
            url=params.get("url")
            if not url:
                return {"status": "error", "message": "Image path is required for image_caption"}
            response = perform_upstage_ocr(url)
            return {"status": "success", "data": response}
        elif tool_name == "webscraper":
            url=params.get("url")
            if not url:
                return {"status": "error", "message": "url is required for webscraper"}
            response=scrape_all_content(url)
            return {"status": "success", "data": response}
        elif tool_name == "finance_news":
            query=data.get("message")
            if not query:
                return {"status": "error", "message": "message   is required for Finance_news"}
            response = get_finance_news(query)
            return {"status": "success", "data": response}
        # # elif tool_name == "books":
        # #     query=data.get("message")
        # #     if not query:
        # #         return {"status": "error", "message": "query is required to search Books"}
        # #     response=search_books(query)
        #     return {"status": "success", "data": response}
        elif tool_name == "extract":
            url=params.get("url")
            file_type=params.get("file_type")
            response = read_document(url, file_type, clean=True)
            return response
        # elif tool_name == "sentiment":
        #     query=data.get("message")
        #     if not query:
        #         return {"status": "error", "message": "query is required for sentiment analysis."}
        #     response=sentiment(query)
        #     return response
        elif tool_name == "image_generation":
            query=data.get("message")
            response=generate_image(query)
            return response
        elif tool_name == "website_screenshot":
            url=params.get("url")
            response=take_screenshot(url)
            return response
        else:
            return {"status": "error", "message": "Unknown tool specified."}
    
        

    except Exception as e:
        return {"status": "error", "message": f"An error occurred: {str(e)}"}
