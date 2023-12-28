import os
import json
import requests
import random
import time

from flask import Flask, abort, redirect, render_template, session, url_for, request

app = Flask(__name__)

app.secret_key = "secretstuff"

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ''
    first_number = random.randint(60,100)
    second_number = random.randint(60, 100)
    answer = first_number + second_number

    user_ans = request.form.get("ans")
    if user_ans == answer:
        result = True
    else:
        result = False
    
    time.sleep(2)
    return render_template('index.html', 
                           first_number=first_number,
                           second_number=second_number,
                           result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
