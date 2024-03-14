import os
import click # Facilitates the creation of command line interfaces.
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def connect_db():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST")
        )
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

@click.group()
def cli():
    pass

@cli.command() # Define a new click command.
@click.option('--name', required=True, help="Name of game") # option need --, is the same that argument.
@click.option('--genre', required=True, help="Genre of game")
@click.option('--platform', required=True, help="Type of platform")
@click.option('--release_year', required=True, help="Release year of game")
@click.pass_context

def newgame(ctx, name, genre, platform, release_year):
    if not name or not genre or not platform or not release_year:
        ctx.fail("The fields indicated are required")
    else:
        conn = connect_db()
        if conn is None:
            print("Unable to connect to the database")
            return

        try:
            cur = conn.cursor()
            cur.execute("INSERT INTO videogames (name, genre, platform, release_year) VALUES (%s, %s, %s, %s)", (name, genre, platform, release_year))
            conn.commit() 
            print(f"Game {name} {genre} {platform} {release_year} created successfully")
        except psycopg2.Error as e:
            print(f"Error while creating the game: {e}")
        finally:
            conn.close()

@cli.command()
def videogames():
    conn = connect_db()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM videogames")
            rows = cur.fetchall() # retrieves all rows of a query
            for row in rows:
                print(f"{row[0]} - {row[1]} - {row[2]} - {row[3]} - {row[4]} ")
        except psycopg2.Error as e:
            print(f"Error reading games from database: {e}")
        finally:
            conn.close()
    else:
        print("Unable to connect to the database")

@cli.command()
@click.argument('name') # argument don't need --, is the same that option.
def game(name):
    conn = connect_db()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM videogames WHERE name = %s", (name,))
            row = cur.fetchone() # Returns the next resulting row
            if row:
                print(f"{row[0]} - {row[1]} - {row[2]} - {row[3]}")
            else:
                print(f"The game {name} was not found")
        except psycopg2.Error as e:
            print(f"Error when reading the set from the database: {e}")
        finally:
            conn.close()
    else:
        print("Unable to connect to the database")



@cli.command()
@click.argument('name')
@click.option('--genre', help='game genre')
@click.option('--platform', help='game platform')
@click.option('--release_year', help='game release year')
def update(name, genre, platform, release_year):
    conn = connect_db()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("UPDATE videogames SET genre = %s, platform = %s, release_year = %s WHERE name = %s", (genre, platform, release_year, name)) # SET indicates that the columns name, genre, platform and year of release will be updated.
            conn.commit()
            print(f"The game {name} was updated successfully")
        except psycopg2.Error as e:
            print(f"Error when updating the game in the database: {e}")
        finally:
            conn.close()
    else:
        print("Unable to connect to the database")



@cli.command()
@click.argument('name') # argument don't need --, is the same that option.
def delete(name):
    conn = connect_db()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("DELETE FROM videogames WHERE name = %s", (name,))
            conn.commit()
            print(f"The game {name} has been deleted successfully")
        except psycopg2.Error as e:
            print(f"Error deleting game from database: {e}")
        finally:
            conn.close()
    else:
        print("Unable to connect to the database")
       

                                                                
if __name__ == '__main__': # The code inside if __name__ == '__main__ will not be executed automatically in case of module import
    cli()