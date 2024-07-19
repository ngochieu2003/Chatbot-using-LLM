import gemini_structured.data_engine.loader as loader

majors_df = loader.load_multiple_csv(["khmt.csv"])

majors_desc = {
    "khmt": "Ngành Khoa học máy tính",
}

import gemini_structured.llm.prompt as prompt
import gemini_structured.llm.llm as llm

query_sys_ins = prompt.extractor_sysins_fmt(majors_desc)
llm.init_query_gen(query_sys_ins)
