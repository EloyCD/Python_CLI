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



