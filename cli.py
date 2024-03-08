import click # It is not the same as CLI, CLICK IS THE LIBRARY.
import json_settings

@click.group()
def cli():
     pass

@cli.command() # The command will read the json file.
def videogames():
    videogames = json_settings.read_json()
    print(videogames)

if __name__== '__main__': # It is used to indicate that it is the main module.
   cli()








