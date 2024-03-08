import click # It is not the same as CLI, CLICK IS THE LIBRARY.

@click.group()
def cli():
     pass

if __name__== '__main__': # It is used to indicate that it is the main module.
   cli()

@cli.command() # The command will read the json file.
def videogames():







