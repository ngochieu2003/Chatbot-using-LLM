def load_csv(filename: str):
    import pandas as pd
    filename = f"data/{filename}"
    return pd.read_csv(filename)

def load_multiple_csv(filenames: list[str]):
    return {filename.split(".")[0]: load_csv(filename) for filename in filenames}
