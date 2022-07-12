from unittest import result
from flask import Flask, request, json
import services, urls
from urls import course

app=Flask(__name__)

@app.route('/')
def welcome():
    return "hmmmm"

app.register_blueprint(course, url_prefix = "/course")

if __name__=='__main__':
    app.run(debug=True)