import os
from openai import AsyncAzureOpenAI

client=AsyncAzureOpenAI(azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),api_key=os.getenv("AZURE_OPENAI_API_KEY"),api_version="2025-01-01-preview")

async def ask(prompt:str):
    deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT","gpt-5")
    resp=await client.chat.completions.create(model=deployment,messages=[{"role":"user","content":prompt}])
    return resp.choices[0].message.content
