from fastapi import APIRouter
from pydantic import BaseModel

chat_router = r = APIRouter()

from gemini_structured import majors_df
from gemini_structured.llm.llm import llm_query_gen
import gemini_structured.query.query_executor as qe
import pandas as pd

class Response(BaseModel):
    message: str

@r.post("")
async def chat_request(question):
    print(f"prompt: {question}")
    print("===")
    response = llm_query_gen.generate_content(question)
    query_json = response.text
    print(query_json)
    print("===")
    result = qe.execute_json(query_json, majors_df)
    print(result)

    if type(result) == pd.DataFrame:
        result = result.to_markdown()
    elif result == None:
        return Response(message="Không thể trả lời!")

    result = str(result)
    print(result)

    return Response(message=result)
