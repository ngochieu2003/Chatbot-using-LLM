# from gemini_structured.llm.llm import gemini_init

from dotenv import load_dotenv
load_dotenv()

import gemini_structured.data_engine.loader as loader
import gemini_structured.llm.prompt as prompt

majors_df = loader.load_multiple_csv(["khmt.csv"])
#
# print(list(dataframes.keys()))
# print(dataframes["khmt"].head())

majors_desc = {
    "khmt": "Ngành Khoa học máy tính",
}

import gemini_structured.query.query_executor as qe
import json

cmd = {
    "major": "khmt",
    "columns": [
        "Mã học phần"
    ],
    "filters": {
        "column": "Số tín chỉ",
        "filter": 2,
        "type": "le"
    },
    "query_type": "sum"
}
s = json.dumps(cmd)

print(qe.execute_json(s, majors_df))
