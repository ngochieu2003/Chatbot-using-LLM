import os
import google.generativeai as genai

genai.configure(api_key=os.environ['GOOGLE_API_KEY'], transport="rest")

llm_query_gen: genai.GenerativeModel
llm_answer_gen: genai.GenerativeModel

def init_query_gen(system_ins: str):
    global llm_query_gen
    llm_query_gen = genai.GenerativeModel(model_name='gemini-1.5-flash',
                                          system_instruction=system_ins,
                                          generation_config={"response_mime_type": "application/json"})
