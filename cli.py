import click
import json_settings

@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', required=True, help="Name of game") # option need --, is the same that argument.
@click.option('--genre', required=True, help="Genre of game")
@click.option('--platform', required=True, help="Type of platform")
@click.option('--release_year', required=True, help="Release year of game")
@click.pass_context
def newgame(ctx, name, genre, platform, release_year):
    if not name or not genre or not platform or not release_year:
        ctx.fail("The fields indicated are required")
    else:
        videogames = json_settings.read_json()
        new_game = {
            'name': name,
            'genre': genre,
            'platform': platform,
            'release_year': release_year
        }
        videogames.append(new_game)
        json_settings.write_json(videogames)
        print(f"Game {name} {genre} {platform} {release_year} created successfully")

@cli.command()
def videogames():
    videogames = json_settings.read_json()
    for game in videogames:
        print(f"{game['name']} - {game['genre']} - {game['platform']} - {game['release_year']}")

@cli.command()
@click.argument('name') # argument don't need --, is the same that option.
def game(name):
    videogames = json_settings.read_json()
    # The function x for x in videogames, if the element that you are traversing with its property name == name that we are receiving, will give us the concrete videogame, otherwise it will give None.
    game = next((x for x in videogames if x ['name'] == name ), None)# Next() is used to sequentially access each element of our list.
    if game is None:
        print(f"The game {name} was not found")
    else:
        print(f"{game['name']} - {game['genre']} - {game['platform']} - {game['release_year']}")

                                                                
if __name__ == '__main__':
    cli()









