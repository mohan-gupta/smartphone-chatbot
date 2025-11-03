from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from cfg import google_api_key

def get_llm(temperature=0.3, model_name="gemini-2.5-flash-lite"):
    llm = ChatGoogleGenerativeAI(api_key=google_api_key, model=model_name, temperature=temperature)
    
    return llm

async def run_llm_chain(parameters, inputs, template, model="gemini-2.5-flash-lite", temperature=0.3,) -> str:
    llm = get_llm(temperature=temperature, model_name=model)
    
    query_prompt = PromptTemplate.from_template(template)
    
    chain = (
            parameters
            | query_prompt
            | llm
            | StrOutputParser()
    )
    
    result = await chain.ainvoke(inputs)
    
    return result
