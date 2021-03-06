#!/usr/bin/env python3

from flask import Flask, render_template


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'secretkey'


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
  app.run()
