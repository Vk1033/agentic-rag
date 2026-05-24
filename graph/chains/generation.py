from langchain_core.output_parsers import StrOutputParser
from langsmith import Client
from langchain_nvidia_ai_endpoints import ChatNVIDIA

client = Client()
prompt = client.pull_prompt("rlm/rag-prompt", dangerously_pull_public_prompt=True)

llm = ChatNVIDIA(
    model="mistralai/mistral-nemotron",
    temperature=1,
    top_p=0.9,
    max_completion_tokens=16384,
)

generation_chain = prompt | llm | StrOutputParser()
