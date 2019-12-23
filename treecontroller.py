#!/usr/bin/env python3

from flask import Flask
from subprocess import *

app = Flask(__name__)

@app.route('/')
def index():
    return "XMas Tree Thing!\nCall either /treeon or /treeoff to do A Thing.\n"

@app.route('/treeon')
def treeon():
    cmd = "./lighttree.py &"
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return "Tree ON!\n"

@app.route('/treeoff')
def treeoff():
    cmd = "./treeoff.py &"
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0] 
    return "Tree OFF!\n"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
 
