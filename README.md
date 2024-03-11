# Python_CLI

In this exercise, we will create a Console or Terminal application that allows us to do CRUD (Create, Read, Update, Delete) operations using commands and parameters. This application is a good practice for those developers who know the basics of Python, such as loops, functions, dictionaries, reading files, modules, and now want to create their first application using these concepts. For this project we will also be using the pip package called click, which facilitates the creation of terminal commands and parameters.

### `Prerequisites:`

Make sure you have Python installed on your system. You can download it from python.org. You will also need pip, the Python package manager.

### `Click Installation:`

Before we start, we will need to install Click. You can do this by running the following command in your terminal:

PIP INSTALL CLICK

### `Project Structure:`

1. cli.py: This will be the main file of our application, where we will define the commands and their functionalities.

2. json_settings.py: This file will contain the functions to read and write data in a JSON file.

### `Command Creation:`

In the cli.py file, we will use Click to define our commands. For example, we will create a newgame command to add a new game to our list of video games and a videogames command to display all existing video games.

### `Data Management with JSON Files:`

We will use a JSON file called videogames.json to store the data of our video games. The file will contain a list of dictionaries, where each dictionary will represent a videogame with its attributes such as name, genre, platform and year of release.

### `Application Execution:`

Once we have defined our commands and functions, we can run our application from the terminal. For example:

```
python cli.py newgame --name "FIFA" --genre "Sports" --platform "PlayStation 4" --release_year "2020"

```

This command will add a new game called "FIFA" to our list of video games.

```
python cli.py videogames

```

This command will show all the existing video games in our list.

## Visualize a Game

This command allows you to view the details of a specific game stored in the game list.

```
python cli.py game --name "Game Name"

```

### `Parameters:`

--name: Specifies the name of the game for which you want to see the details.

If the game is found in the list of video games, details such as name, genre, platform and year of release will be displayed. If the game is not found, a message will be printed indicating that the game was not found.

## Updating a Game

This command allows you to update the details of an existing game in the game list.

```
python cli.py update --name "Game Name" [--genre "Game Genre"] [--platform "Game Platform"] [--release_year "Release Year"]

```

### `Parameters:`

--name: Specifies the name of the game to update.

--genre: (Optional) The new genre of the game.

--platform: (Optional) The new platform of the game.

--release_year: (Optional) The new release year of the game.

## Delete a Game

This command allows you to remove a game from the list of video games.

```
python cli.py delete --name "Game Name"

```
### `Parameters:`

--name: Especifica el nombre del juego que se desea eliminar.

This command will remove the game from the list of video games, if the game is found in the list. If the game is not found, a message will be printed indicating that the game was not found.







