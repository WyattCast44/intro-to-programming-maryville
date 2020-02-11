from console import Console

class Help(Console):

    description = 'Display the application help screen'
    
    signature = {
        'h': 'Display the application help screen'
    }

    def __init__(self, application):
        self.application = application

    def handle(self):
        Console().line(f'\nRunning the help command\n{self.application.config["name"]}')