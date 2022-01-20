from unittest import result
from flask import Flask, jsonify, request
import time

app = Flask(__name__)
@app.route("/bot". method=["post"])

# response
def response():
   query = dict(request.form)['query']
   result = query + " " +time.ctime()
   return jsonify({"response" :result })

if __name__ == "__main__":
    app.runhost("0.0.0.0.")