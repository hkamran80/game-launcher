"""
Game Library Settings
Contributors:
    :: H. Kamran [@hkamran80] (author)
Version: 0.1.0
Last Updated: 2020-02-25, @hkamran80
"""

# EDIT THIS
ORIGIN_LIBRARY_PATH = ""
STEAM_LIBRARY_PATH_PREFIX = ""

IGDB_API_KEY = ""
COVER_DOWNLOAD_LOCATION = "[path-to-assets/covers]/assets/covers"

# macOS Example: /Applications/Steam.app
STEAM_APPLICATION_PATH = ""

WEB_HOST = "127.0.0.1"
WEB_PORT = 8017
WEB_DEBUG = True

# DO NOT EDIT PAST HERE
COMPATIBLE_LAUNCHERS = ("STEAM", "ORIGIN")
STEAM_LIBRARY_PATH_SUFFIX = "steamapps/"
STEAM_LIBRARY_PATH = STEAM_LIBRARY_PATH_PREFIX + STEAM_LIBRARY_PATH_SUFFIX
STEAM_LIBRARY_GAMES_PATH = STEAM_LIBRARY_PATH + "common/"