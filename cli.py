import click
import json_settings

@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', required=True, help="Name of game")
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

if __name__ == '__main__':
    cli()









