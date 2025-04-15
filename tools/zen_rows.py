from composio_langchain import ComposioToolSet, Action, App


tool_set=ComposioToolSet()



def run(message:str,params:dict):
    params={
    "url":message
}
    response=tool_set.execute_action(
        action="ZENROWS_SCRAPE_URL",
        params=params,
        entity_id="default"
)
    return response

