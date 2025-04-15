from composio import ComposioToolSet,Action,App

tool_set=ComposioToolSet()


def run(message:str,params:dict):
    numberofdays=params.get("numberofdays")
    params={
    "numOfDays":numberofdays
}
    response=tool_set.execute_action(
        action="MICROSOFT_CLARITY_DATA_EXPORT",
        params=params,
        entity_id="default"
)
    return response

