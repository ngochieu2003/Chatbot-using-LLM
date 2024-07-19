from dotenv import load_dotenv
load_dotenv()

#
# import gemini_structured.query.query_executor as qe
#
# prompt = "Danh sách những học phần Vật lý"
# print(f"prompt: {prompt}")
# print("===")
# response = llm.llm_query_gen.generate_content(prompt)
# query_json = response.text
# print(query_json)
# print("===")
# result = qe.execute_json(query_json, majors_df)
# print(result)

import os
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from gemini_structured.api.chat import chat_router
import uvicorn

app = FastAPI()

app.include_router(chat_router, prefix='/api/chat')

@app.get("/")
async def redirect_to_docs():
    return RedirectResponse(url="/docs")

if __name__ == "__main__":
    app_host = os.getenv("APP_HOST", "0.0.0.0")
    app_port = int(os.getenv("APP_PORT", "8000"))
    reload = True 

    uvicorn.run(app="main:app", host=app_host, port=app_port, reload=reload)
