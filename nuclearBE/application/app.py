from flask import json, Flask, request
from loguru import logger

from application.routes.user import user_api

app = Flask(__name__)
app.register_blueprint(user_api)

# configure logger
logger.add("job.log", format="{time} - {message}")


@app.route("/hello_world", methods=["POST"])
def hello_world():
    logger.info('hello world endpoint invoked!')
    res = {'hello': 'world!'}
    return json.dumps(res), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True, port=5000)
