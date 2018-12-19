from flask import Flask
import platform
import datetime
application = Flask(__name__)

@application.route("/")
def hello():
    res = '''
    date: %s
    version: %s
    platform: %s
    uname: %s
    processor: %s
    node: %s''' % (
        datetime.datetime.now(),
        platform.version(),
        platform.platform(),
        platform.uname(),
        platform.processor(),
        platform.node(),
    )
    return res

if __name__ == "__main__":
    application.run()
