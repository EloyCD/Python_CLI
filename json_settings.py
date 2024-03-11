import json  # Module that allows us to read json files
import os # Module interacts with the operating system, in this case, we are going to manipulate file paths.


def read_json():
    if not os.path.isfile('videogames.json'):  # If the json file does not exist, I want you to create it for me.
        with open('videogames.json' , 'w') as f:
            json.dump([], f) # It would be the object videogames.json and writes it to the file videogames.json
    with open('videogames.json', 'r') as f:
        videogames = json.load(f)
        return videogames if isinstance(videogames, list) else [] # Returns an empty list if videogames is not a list, and does nothing if videogames is a list.
        
        

def write_json(new_data):
    with open('videogames.json', 'w') as f:
        json.dump(new_data, f)

