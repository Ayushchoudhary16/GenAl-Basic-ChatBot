import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

bot=ChatOpenAI(model="gpt-3.5-turbo",api_key=os.getenv("OPENAI_API_KEY"))