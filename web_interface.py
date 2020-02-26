"""
Game Library Web Interface
Contributors:
    :: H. Kamran [@hkamran80) (author)
Version: 0.1.0
Last Updated: 2020-02-23, @hkamran80
"""

from flask import Flask, request, redirect, url_for, render_template
from steamfiles import acf
import subprocess
import time
import os

import settings
import backend

app = Flask(__name__, static_url_path="/assets", static_folder="assets")

@app.route("/", methods=["GET"])
def index():
    return render_template("library.html", catalog=backend.get_games_from_launchers())

@app.route("/launch", methods=["GET"])
def launch():
    if not request.args.get("launcher") or not request.args.get("game_identifier"):
        return "404"

    launcher = request.args.get("launcher")
    game_identifier = request.args.get("game_identifier")

    if request.args.get("launcher") == "STEAM":
        _acf = acf.load(open(settings.STEAM_LIBRARY_PATH + f"appmanifest_{request.args.get('game_identifier')}.acf"))
        _path = settings.STEAM_LIBRARY_GAMES_PATH + _acf["AppState"]["installdir"] + "/"
        
        for _file in os.listdir(_path):
            if _file[0] != "." and _file.split(".")[-1]: 
                path = _path + _file

        subprocess.Popen(["open", settings.STEAM_APPLICATION_PATH], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(30)
    elif request.args.get("launcher") == "ORIGIN":
        print(settings.ORIGIN_LIBRARY_PATH)
        print(game_identifier)
        path = settings.ORIGIN_LIBRARY_PATH + game_identifier + ".app"

    subprocess.Popen(["open", path], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

    return "200"

if __name__ == "__main__":
    app.run(host=settings.WEB_HOST, port=settings.WEB_PORT, debug=settings.WEB_DEBUG)