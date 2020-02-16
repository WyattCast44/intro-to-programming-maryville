from .input import ConsoleInput
from .output import ConsoleOutput

class Console(ConsoleInput):
    
    # Options holds the console
    # registered options
    options = {}

    # Commands holds the console
    # registered commands
    commands = {}

    def output(self):
        return ConsoleOutput()

    # 
    # COMMANDS
    # 

    def registerCommand(self, key, handler):
        self.commands[key] = handler

        return self

    def registerCommands(self, commands):

        if type(commands) == list:
            
            # Given the list, use the class
            # to get the signature for the command
            for command in commands:
                self.registerCommand(key=command.signature, handler=command)

        elif type(commands) == dict:

            # Given the dict, use the provided key
            # and set the handler
            for key, command in commands.items():
                self.registerCommand(key=key, handler=command)
        
        return self
    
    def runCommand(self, command):
        
        # Ensure that command is registered
        if command in self.commands:
            
            # Check if handler is a class
            if isinstance(self.commands[command], type):
                self.commands[command](self).handle()
                return
            
            # Check if handler is a function
            elif callable(self.commands[command]):
                self.commands[command](self)
                return

            # Unknown handler type
            else:
                raise Exception(f'Unable to handle command with given handler. Command: {command}, Handler: {self.commands[command]}')
        
        else:
            raise Exception(f'Unknown command: {command}')