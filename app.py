from flask import Flask
import json
from azure.identity import ClientSecretCredential
app = Flask(__name__)


@app.route("/")
def index():
    
    credentials = ClientSecretCredential("a572004d-6f4c-4446-824a-c5a9cac4ff21", "5a54f6b8-a6ac-4dd9-aec6-7cf8063953f6", "xkG7Q~8Xg0C5~hkjZ.pgCvPYJ8MdqoJZlhvxQ")
    print(credentials.get_token())
    data = '{ "name":"Pratyush", "age":30, "city":"New York"}'
    y = json.loads(data)
    print (y)
    return y


if __name__ == "__main__":
    app.run(host="0.0.0.0")

