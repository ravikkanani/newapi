from flask import Flask, jsonify, request
import requests
import json
import sys
from bs4 import BeautifulSoup
from cricbuzz import Cricbuzz
from flask import Response
app = Flask(__name__)

@app.route('/12')
def getMatches():
    c = Cricbuzz()
    list =  c.matches()
    return Response(json.dumps(list),  mimetype='application/json')


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("1234")
    )


