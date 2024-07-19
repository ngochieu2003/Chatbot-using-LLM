import pandas as pd
import json

filter_type = {
    'eq': lambda x, y: x == y,
    'neq': lambda x, y: x != y,
    'lt': lambda x, y: x < int(y),
    'gt': lambda x, y: x > int(y),
    'le': lambda x, y: x <= int(y),
    'ge': lambda x, y: x >= int(y),
    'in': lambda x, y: x.apply(lambda s: y in s),
}

def _filter_df(df: pd.DataFrame, filter: dict):
    cmp = filter_type[filter['type']]
    if df[filter['column']].dtypes != 'object':
        filter['filter'] = int(filter['filter'])
    return df[cmp(df[filter['column']], filter['filter'])]

def _coerce_df(df: pd.DataFrame, query_type: str):
    if query_type == 'all':
        return df
    elif query_type == 'sum':
        return df.sum()
    elif query_type == 'count':
        return df.shape[0]

def execute_json(commmand_json: str, majors: dict[str, pd.DataFrame]):
    command = json.loads(commmand_json)
    result = None
    try:
        if command["query_type"] == "unknow":
            return None
        # For testing
        command["major"] = 'khmt'
        if command["major"] not in majors.keys():
            return "Hãy cung cấp ngành học mà bạn muốn hỏi"
        result = majors[command["major"]]

        filter = command['filter']
        if type(filter) == list and len(filter) > 0:
            filter = filter[0]
        if type(filter) == dict and len(filter.keys()) == 3:
            result = _filter_df(result, filter)

        if len(command["columns"]) > 0:
            result = result[command["columns"]]

        if type(result) != pd.DataFrame:
            return result

        result = _coerce_df(result, command["query_type"])
    except Exception as e:
        print("Something went wrong when executing json:")
        print(commmand_json)
        print(e)
        return None
    return result
