import os

from flask import Flask, render_template, request
import socket

VERSION = os.environ["VERSION"]

app = Flask(__name__)


@app.route("/")
def index():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return render_template(
            "index.html",
            hostname=host_name,
            ip=host_ip,
            version=VERSION,
            user_ip=request.remote_addr,
        )
    except:
        return render_template("error.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
