import json

from langchain_core.runnables import RunnablePassthrough

import prompt_templates as templates

from llm_stack import run_llm_chain

from techspec_api import get_smartphone_details
from cfg import logger

async def classify_query_chain(query: str)-> str:
    parameters = {"query": RunnablePassthrough()}
    inputs = {"query": query}
    
    response = await run_llm_chain(
        parameters=parameters, inputs=inputs, template=templates.classify_query_template
    )
    
    response = response.removeprefix("response:")
    response = response.strip()
    
    return response

async def identify_smartphone_chain(query: str)-> str:
    parameters = {"query": RunnablePassthrough()}
    inputs = {"query": query}
    
    response = await run_llm_chain(
        parameters=parameters, inputs=inputs, template=templates.identify_smartphone_template
    )
    
    response = response.removeprefix("```json")
    response = response.removesuffix("```")
    
    json_response = json.loads(response)
    
    return json_response

async def smartphone_chain(query: str, smartphone_data)-> str:
    parameters = {"query": RunnablePassthrough(), "smartphone_data": RunnablePassthrough()}
    inputs = {"query": query, "smartphone_data": smartphone_data}
    
    response = await run_llm_chain(
        parameters=parameters, inputs=inputs, template=templates.phone_template
    )
    
    return response

async def smartphone_assistant(query: str):
    query_type = await classify_query_chain(query=query)
    
    if query_type == "invalid":
        return "I can only help you with smartphones related queries. Please, ask a query related to smartphones."
    
    smartphone_names = await identify_smartphone_chain(query=query)
    
    smartphone_data = {}
    if smartphone_names is not None:
        for name in smartphone_names:
            try:
                smartphone_data = get_smartphone_details(smartphone_name=name)
                smartphone_data[name] = smartphone_data
            except Exception as e:
                logger.error(f"Error occurred while fetching smartphone data; error details: {e}")
            
    response = await smartphone_chain(query=query, smartphone_data=smartphone_data)
    return response

