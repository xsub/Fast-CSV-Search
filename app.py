# Pawel Suchanecki <psuchanecki@almalinux.org>
from fastapi import FastAPI
import pandas as pd
import time

# Do benchmark?
b = True

app = FastAPI()

# Load CSV file into a Pandas DataFrame
data = pd.read_csv("file.csv")

# Build the list of columns from first row of file.csv
columns = data.columns.tolist()

@app.get("/")
def read_root():
    return {"message": "Welcome to the AlmaLinux Driver List Search API"}

@app.get("/search/")
def search(query: str = ""):
    if b:
        start_time = time.time() # Start the timer

    if query == "":
        result = {"results": data.to_dict(orient="records")}
    else:
        search_query = query.strip().lower()
        mask = False

        for column in columns:
            mask |= data[column].astype(str).str.contains(search_query, case=False)
            #  Break the search on first column that matches -- great optimization! :)
            if mask.any():
                break

        search_result = data[mask]
        result = {"results": search_result.to_dict(orient="records")}

    if b:
        end_time = time.time() # End the timer
        elapsed_time = end_time - start_time

        print(f"PERF:\t  Query served in {elapsed_time*1000:.1f} miliseconds") # Print the elapsed time to console

    return result
