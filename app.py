from flask import Flask
from azure.storage.filedatalake import DataLakeServiceClient
import json
import csv
import pandas as pd
app = Flask(__name__)


@app.route("/")
def index():
    
    data = '{ "name":"Pratyush", "age":30, "city":"New York"}'
    y = json.loads(data)
    print (y)
    return y


if __name__ == "__main__":
    app.run(host="0.0.0.0")

