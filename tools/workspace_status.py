from composio_langchain import ComposioToolSet, Action, App


tool_set=ComposioToolSet()



def run(message:str,params:dict):
    params={
    "workspace_id":message
}
    response=tool_set.execute_action(
        action="WORKSPACE_TOOL_WORKSPACE_STATUS_ACTION",
        params=params,
        entity_id="default"
)
    return response

