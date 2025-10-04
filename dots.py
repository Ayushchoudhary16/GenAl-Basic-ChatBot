from pydantic import BaseModel

class QuestionDTO(BaseModel):
    question: str
