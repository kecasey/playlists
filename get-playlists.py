from gmusicapi import Mobileclient
from datetime import date
import fileinput

for line in fileinput.input():
    print(line)

lists_to_get = ['Party Mix','Rap','Blues','Ivy music']

api = Mobileclient()
#TODO read pw from command line
logged_in = api.login('kevinecasey@gmail.com','zehovhwxlowhszfi',Mobileclient.FROM_MAC_ADDRESS)

if logged_in:
    
    print("Getting playlists...\n")
    all_playlists = api.get_all_user_playlist_contents()
    print("Getting library (for track lookup)...\n")
    my_library = api.get_all_songs()
    
    for playlist in all_playlists:
        if playlist['name'] in lists_to_get:
            print("Parsing playlist "+playlist['name']+"...\n")
            count = 0
            f = open(date.isoformat(date.today())+" -- "+playlist['name'],'w')
            for i in playlist['tracks']:
                track = i.get('track')
                if not track:
                    lib_track = [item for item in my_library if item.get('id') in i.get('trackId')]
                    track = lib_track[0]
                f.write(str(count+1)+","+track['artist']+","+track['album']+","+track['title']+"\n")
                count+=1
            f.close()            
                
api.logout()
