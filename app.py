from flask import Flask, render_template, url_for
from azure.identity import DefaultAzureCredential
from azure.storage.filedatalake import DataLakeServiceClient
import json
import csv
import pandas as pd
app = Flask(__name__)


@app.route("/")
def index():
    
    data = '{ "name":"Jonas", "age":30, "city":"New York"}'
    y = json.loads(data)
    print (y)
    return y


if __name__ == "__main__":
    app.run(host="0.0.0.0")
