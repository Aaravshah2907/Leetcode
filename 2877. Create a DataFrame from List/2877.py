import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    columnHeaders = ["student_id","age"]
    result = pd.DataFrame(student_data, columns = columnHeaders)
    return result