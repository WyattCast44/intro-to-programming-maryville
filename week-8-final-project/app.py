from cliff import Application
from tinydb import TinyDB, Query, where
from cliff.commands import MakeCommand
from commands import ResumeGame, StartNewGame, ShowCredits

# Init the database
db = TinyDB('db.json')

app = Application({
    'name': 'Final Project',
    'description': 'An interactive game for my final project',
    'version': '0.1.0',
    'interactive': True
}).registerCommands([
    StartNewGame,
    ResumeGame,
    ShowCredits
])

app.state().set('db', db)

app.state().get('db').update({'name': 'Wyatt'}, where('name') == 'James')

app.run()
