from composio import ComposioToolSet,Action,App

tool_set=ComposioToolSet(api_key="jzjstcadadwfz5arkpfse")

def run(message:str,params:dict):
    query={
        "query":message
    }
    response=tool_set.execute_action(
        action="SERPAPI_IMAGE_SEARCH",
        params=query,
    
)
    return response
