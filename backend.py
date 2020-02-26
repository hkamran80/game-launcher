"""
Game Library Backend
Contributors:
    :: H. Kamran [@hkamran80] (author)
Version: 0.1.0
Last Updated: 2020-02-23, @hkamran80
"""

import os
from steamfiles import acf

import settings
import get_cover_art

def get_origin_games():
    _origin_games = []

    for _file in os.listdir(settings.ORIGIN_LIBRARY_PATH):
        if _file[0] != ".":
            _origin_games.append(_file.replace(".app", "").replace(".exe", ""))
    
    return _origin_games

def get_steam_games():
    _steam_games = []

    for _file in os.listdir(settings.STEAM_LIBRARY_PATH):
        if _file[0] != "." and _file.split(".")[-1] == "acf":
            _acf = acf.load(open(settings.STEAM_LIBRARY_PATH + _file))
            _steam_games.append((_acf["AppState"]["name"], _acf["AppState"]["appid"]))

    return _steam_games

def get_games_from_launchers(launchers: list=settings.COMPATIBLE_LAUNCHERS):
    games = {}

    if "ORIGIN" in launchers:
        games["ORIGIN"] = get_origin_games()
    
    if "STEAM" in launchers:
        games["STEAM"] = get_steam_games()
    
    return games

if __name__ == "__main__":
    all_games = get_games_from_launchers()

    for _launcher in all_games:
        launcher = all_games[_launcher]
        if _launcher == "STEAM":
            for game in launcher:
                get_cover_art.download_steam_cover_art(game[1])
        else:
            for game in launcher:
                get_cover_art.download_igdb_cover_art(game, _launcher)
