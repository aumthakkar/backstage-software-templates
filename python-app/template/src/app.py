
from flask import Flask, jsonify
import time
import socket

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, which tells the application which URL should call 
# the associated function.
@app.route('/api/v1/info')
# ‘/’ URL is bound with hello_world() function.
def info():
    return jsonify({
        'time' : time.ctime(),
        'hostname' : socket.gethostname(),
        'message' : 'You are doing great, Pranav! <3',
        'deployed_on' : 'kubernetes'
        'env': '${{values.app_env}}',
        'app_name': '${{values.app_name}}'
    })

@app.route('/api/v1/healthz')
# ‘/’ Do an actual test here.
def health():
    return jsonify({
        'status' : 'up'}), 200

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server by default
    # If you want that app to be accessible from the internet on your browser then host="0.0.0.0" should be configured as shown below:
    app.run(host="0.0.0.0")