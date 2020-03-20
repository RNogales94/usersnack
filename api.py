from flask import Flask, request, redirect, Response, abort
import json
import os


app = Flask(__name__)


@app.route("/")
def index():
    return Response(json.dumps({}), status=200)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    env = os.environ.get('ENVIRONMENT', 'DEV')
    if env == 'PRD':
        debug = False
        host = '0.0.0.0'
    else:
        debug = True
        host = '127.0.0.1'

    app.run(host=host, port=port, debug=debug)
