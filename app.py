from flask import Flask
import json
from azure.identity import ClientSecretCredential
app = Flask(__name__)


@app.route("/")
def index():
    try:
        print("Inside code")
        credentials = ClientSecretCredential("a572004d-6f4c-4446-824a-c5a9cac4ff21", "5a54f6b8-a6ac-4dd9-aec6-7cf8063953f6", "xkG7Q~8Xg0C5~hkjZ.pgCvPYJ8MdqoJZlhvxQ")
        print(credentials._client_id)
        data = '{ "name":"Pratyush", "age":300, "city":"New York"}'
        y = json.loads(data)
        print (y)
        return credentials._client_id
    except Exception as e:
        print(e)


if __name__ == "__main__":
    app.run(host="0.0.0.0")

