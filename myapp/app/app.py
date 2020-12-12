import sys
from flask import Flask, request
app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def hello_world():
    version = "{}.{}".format(sys.version_info.major, sys.version_info.minor)
    message = "Hello World from Flask in a Docker container running Python {} with Gunicorn (default)</br>".format(
        version
    )
    #print("Here are the Http headers:</br>")
    print(request.headers)
    print(request.headers['User-Agent'])
    
    headers = request.headers
    #headers = headers.replace('\n', '<br />')
    return message + "Request headers:</br>" + str(headers).replace("\n", "</br>")

    #return message + str(headers)
    #return "Hello, World!"

@app.route('/print')
def printMsg():
    app.logger.warning('testing warning log')
    app.logger.error('testing error log')
    app.logger.info('testing info log')
    return "Check your console"

if __name__ == "__main__":
    app.run(host='0.0.0.0')