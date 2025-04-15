 
# os.environ["OPENAI_API_KEY"] = "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"

import typing as t
from composio_openai import ComposioToolSet, action, Action
from openai import OpenAI
import os
import requests

from dotenv import load_dotenv
load_dotenv()

# Load Zoho Books credentials from environment variables
ZOHO_ORG_ID = os.getenv("ZOHO_ORG_ID")
ZOHO_ACCESS_TOKEN = os.getenv("ZOHO_ACCESS_TOKEN")

os.environ["OPENAI_API_KEY"] = "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"

openai_client = OpenAI()
toolset = ComposioToolSet()

@action(toolname="zoho_books")
def create_invoice(
    customer_id: str,
    invoice_date: str,
    line_items: t.List[dict],
    execute_request: t.Callable,
) -> dict:
    """
    Create a new invoice in Zoho Books.

    :param customer_id: The ID of the customer the invoice is for.
    :param invoice_date: The date of the invoice (YYYY-MM-DD format).
    :param line_items: A list of items in the invoice (product, price, quantity).
    :return invoice_data: The created invoice details.
    """
    request_body = {
        "customer_id": customer_id,
        "date": invoice_date,
        "line_items": line_items
    }
    response = execute_request(
        f"https://books.zoho.com/api/v3/invoices?organization_id={ZOHO_ORG_ID}",
        "POST",
        request_body,
        None
    )
    return response

tools = toolset.get_tools(actions=[create_invoice])

task = "Create an invoice for customer ID 123456 with two items."

response = openai_client.chat.completions.create(
    model="gpt-4o",
    tools=tools,
    messages=[
        {"role": "system", "content": "You are a helpful agent."},
        {"role": "user", "content": task},
    ],
)

toolset.execute_action(
    action=create_invoice,
    params={
        "customer_id": "123456",
        "invoice_date": "2025-02-20",
        "line_items": [
            {"name": "Product 1", "rate": 100, "quantity": 2},
            {"name": "Product 2", "rate": 200, "quantity": 1}
        ]
    },
    entity_id="default",
)

result = toolset.handle_tool_calls(response)
print(result)
