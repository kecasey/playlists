import sys
from gmusicapi import Mobileclient
from datetime import date
import fileinput

if len(sys.argv) > 1:

    pw = ""
    for line in fileinput.input():
        pw = line

    api = Mobileclient()
    logged_in = api.login('kevinecasey@gmail.com',pw,Mobileclient.FROM_MAC_ADDRESS)

    if logged_in:
        
        playlists = api.get_all_playlists()
        names = []
        
        for playlist in playlists:
            names.append(playlist['name'])
        
        for name in sorted(names):
            print(name)
                    
    api.logout()

else:
    print("Please include the path to a file containing a Google Music password.")
