# from gemini_structured.llm.llm import gemini_init

from dotenv import load_dotenv
load_dotenv()

import gemini_structured.data_engine.loader as loader
import gemini_structured.llm.prompt as prompt

# dataframes = loader.load_multiple_csv(["khmt.csv"])
#
# print(list(dataframes.keys()))
# print(dataframes["khmt"].head())

majors_desc = {
    "khmt": "Ngành Khoa học máy tính",
}

print(prompt.extractor_sysins_fmt(majors_desc))
