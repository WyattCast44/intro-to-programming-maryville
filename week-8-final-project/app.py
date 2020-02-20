"""
This is a very open-ended problem and intentionally so. The goal is for you to make design choices about how the game plays, how it is themed, and how you structure the data required to make it work. You are encouraged to be as creative as possible in making your adventure game fun and interesting, the theme is entirely up to you. However, you must adhere to a few requirements:

- Your adventurer must have a name, keep track of how many trinkets they've collected, and their personal resource. They can have other
things as well, but these are required.

    - Trinket examples from previous games: Eggo waffles, holiday gifts, and Subway endorsement checks.
    - Personal resouce examples from previous games: time to work on programming assignments, health points, and time for preparing dinner.

- Your enemies must have a name, an introduction (e.g. "It's Aaron Burr! He'll kill your political aspirations and then shoot you in the back!"), and a personal resource that you can reduce when "attacking". Again, other things are also possible and encouraged, but these are required.
    - Enemy examples from previous games: sharks, nosy neighbors, Krampus, and Kylo Ren

- Your adventurer must progress towards something in a 'straight line' (no mazes), no more than 10 steps/moves/transitions/time slices away from the start.

- With each step of progress, it must be possible for the adventurer to collect some amount of your chosen random trinket, or be attacked. Other things can happen as well, but those two must be possible.

- There must be at least three possible enemies you encounter. You should be using some element of random chance so it is possible that on a particular play of the game we might not encounter one or more of the enemies, but there should be at least three possibilities.

- The game must end. It cannot be infinite. Your adventurer may make it to the goal or not make it to the goal, but the game must end at some point without errors (i.e., no Exceptions from Python to end the game).

- Once the game is over, you must at least output the total number of your chosen trinkets the adventurer collected and the final amount of their personal resource. You can output other things as well as they are relevant to your adventure game, but trinket count and personal resource amount are required.
"""

# Standard Libraries
import os, sys

# Other Libraries
from tinydb import TinyDB, Query

# My Libraries
from console import Application

# Commands
from options import Help

# Init the database
db = TinyDB('db.json')

app = Application({
    'name': 'Escape From Mars!',
    'version': '0.1.0',
    'description': 'Escape from Mars is a text based adventure game, where you play Mark Watney, Astronaut.'
})

app.setDefaultCommand(Help).registerOptions([
    Help,
]).run()

# My Libraries
from console import Application

# Options
from options import Help
from options import Version

# # Commands
# from commands import MakeView
# from commands import MakeCommand

# import commands
# def myNewFunction(application):
#     application.console().success('\nhello')

# app = Application({
#     'name': 'Invoice Calculator',
#     'version': '0.1.0',
#     'description': 'Summarize and get insights on your monthly sales invoices'
# })

# app.registerCommands([
#     MakeView,
#     MakeCommand
# ]).registerOptions([
#     Help,
#     Version
# ]).registerOptions({
#     '--b': myNewFunction,
#     '--new': myNewFunction
# }).run()