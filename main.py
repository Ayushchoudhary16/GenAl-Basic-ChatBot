from fastapi import FastAPI
from dots import QuestionDTO
from model import bot

app = FastAPI()

@app.post("/chatbot")
def ask_question(q:QuestionDTO):
    response = bot.invoke(q.question)
    return response.content
