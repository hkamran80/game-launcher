"""
Game Library Helper - Cover Art
Contributors:
    :: H. Kamran [@hkamran80] (author)
Version: 0.1.0
Last Updated: 2020-02-23, @hkamran80
"""

import requests
import settings

def generate_igdb_cover_url(igdb_cover_id: str):
    return f"https://images.igdb.com/igdb/image/upload/t_cover_big/{igdb_cover_id}.jpg"

def igdb_search(query: str=None, limit: int=None):
    url = "https://api-v3.igdb.com/search"
    headers = {"user-key": settings.IGDB_API_KEY}

    igdb_data = "fields game, name;"
    if query:
        igdb_data += f"search \"{query}\";"

    if limit:
        igdb_data += f"limit {str(limit)};"

    r = requests.get(url, headers=headers, data=igdb_data)
    return r.json()

def igdb_cover_art(game_id):
    url = "https://api-v3.igdb.com/covers"
    headers = {"user-key": settings.IGDB_API_KEY}

    r = requests.get(url, headers=headers, data=f"fields game,height,image_id,width;where game={game_id};")
    json_results = r.json()

    if json_results:
        for result in json_results:
            if result["height"] == 800 and result["width"] == 600:
                return generate_igdb_cover_url(result["image_id"])
        
        return generate_igdb_cover_url(json_results[0]["image_id"])
    else:
        return None

def download_igdb_cover_art(game_name: str, launcher: str):
    if launcher in settings.COMPATIBLE_LAUNCHERS and launcher != "STEAM":
        search_results = igdb_search(game_name, 100)
        for result in search_results:
            if result["name"] == game_name:
                cover_art_link = igdb_cover_art(result["id"])
                if cover_art_link != None:
                    _cover_art = requests.get(cover_art_link, allow_redirects=True)
                    open(settings.COVER_DOWNLOAD_LOCATION + "/" + game_name + "." + cover_art_link.split(".")[-1], "wb").write(_cover_art.content)
                    
                    return True
                else:
                    return False
                
        return False
    else:
        return None

def download_steam_cover_art(game_id: str):
    _cover_art = requests.get(f"https://steamcdn-a.akamaihd.net/steam/apps/{game_id}/library_600x900_2x.jpg", allow_redirects=True)
    open(settings.COVER_DOWNLOAD_LOCATION + "/STEAM_" + game_id + ".jpg", "wb").write(_cover_art.content)

    return True