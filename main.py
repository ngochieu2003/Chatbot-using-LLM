# from gemini_structured.llm.llm import gemini_init

from dotenv import load_dotenv
load_dotenv()

import gemini_structured.data_engine.loader as loader

dataframes = loader.load_multiple_csv(["khmt.csv"])

print(list(dataframes.keys()))
print(dataframes["khmt"].head())
