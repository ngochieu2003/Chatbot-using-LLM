from dotenv import load_dotenv
load_dotenv()

import gemini_structured.query.query_executor as qe
import gemini_structured.data_engine.loader as loader

from gemini_structured import majors_desc, majors_df
from gemini_structured.llm import llm, prompt

query_sys_ins = prompt.extractor_sysins_fmt(majors_desc)
llm.init_query_gen(query_sys_ins)

prompt = "Danh sách những học phần Vật lý"
print(f"prompt: {prompt}")
print("===")
# response = llm.llm_query_gen.generate_content(prompt)
# query_json = response.text
query_json = '{"major": "khmt", "columns": ["Mã học phần", "Tên học phần", "Số tín chỉ"], "filter": [{"column": "Số tín chỉ", "filter": "3", "type": "eq"}], "query_type": "all"}'
print(query_json)
print("===")
result = qe.execute_json(query_json, majors_df)
print(result)
