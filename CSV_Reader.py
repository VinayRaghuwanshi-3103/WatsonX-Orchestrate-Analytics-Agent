import os
import json
from ibm_watsonx_orchestrate.agent_builder.tools import tool
import pandas

@tool(name="CSV_Reader",
      description="This tool reads the CSV characterstics and returns the details")

def CSV_Reader(filename: str):
    csvFile = os.path.join(os.path.dirname(__file__), filename)
    contents = os.listdir(os.path.dirname(__file__))
    df = pandas.read_csv(csvFile, low_memory=False)
    # print(df.head(10))
    #return  "File: " + csvFile + ". Folder contents: " + str(contents) + ". Columns: " +str(df.columns)
    #return str(df.info())

    # Get file size in MB
    file_size = os.path.getsize(csvFile) / (1024 * 1024)

    # Get number of rows and columns
    num_rows, num_cols = df.shape

    # Collect column statistics
    columns_info = []
    for col in df.columns:
        col_info = {
            "Column Name": col,
            "Data Type": str(df[col].dtype),
            "Has Blanks": bool(df[col].isnull().any())
        }
        columns_info.append(col_info)

    # Combine results
    stats = {
        "File Size in MB": round(file_size, 3),
        "Number of Columns": num_cols,
        "Rows": num_rows,
        "Column Details": columns_info
    }

    # Return JSON-formatted result
    return json.dumps(stats, indent=4)

#print(test2("Facility Licence-AB.CSV"))
