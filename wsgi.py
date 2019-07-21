# CUNT (Continutally Updating Nature Textposts)
# By: jackzachson (Zach Jackson)

import logging
import config

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(config.APP_NAME)
socketio = SocketIO(app)

# logging config
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)
log_levels = {'debug': logging.DEBUG,
              'info': logging.INFO,
              'warn': logging.WARNING,
              'error': logging.ERROR,
              'critical': logging.CRITICAL}

try:
    logger.setLevel(log_levels[config.LOG_LEVEL])
except KeyError:
    logger.setLevel(logging.INFO)
    logger.error('Invalid logging level, log level set to INFO')
    logger.info("Valid values: 'debug', 'info', 'warn', 'error', or 'critical'")

logger.debug("Logging configuration complete")


################################################################################
@socketio.on('play')
def handle_play(audio, gif):
    logger.info("audio: " + audio)
    logger.info("gif: " + gif)
    socketio.emit('play', (audio, gif))


@socketio.on('message')
def handle_message(message):
    logger.info("message: " + message)
    if message == 'pee':
        socketio.emit("reload")


@app.route("/")
def index():
    logger.info('Script Start')
    return render_template('index.html')


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port='8080')

application = app
