import textwrap

# command lists and aliases
list_move_commands = ['north', 'south', 'east', 'west']
move_alias_dict = {
    'n' : 'north',
    's' : 'south',
    'e' : 'east',
    'w' : 'west',
    'u' : 'up',
    'd' : 'down'
}

# Classes

class Game:
    def __init__(self):
        self.running = True
		
class Room:
    def __init__(self, name):
        self.name = name
        self.description = None
        self.exits = {
            'north' : None,
            'south' : None,
            'east' : None,
            'west' : None
        }
		
    def describe(self):
        print('')
        print(self.name)
        print('=' * len(self.name))
		
        for line in textwrap.wrap(self.description, 80):
            print(line)
		
        print('')
		
        print('Exits from here:')
        print('----------------')
        for k, v in self.exits.items():
            if v == None:
                print(k + ':', 'none visible')
            else:
                print(k + ':', v.name)
				
class Player:
    def __init__(self):
        self.location = None
		
    def move(self): # Outer method
	
        def execute_move(self, destination): # Inner method
            if destination in self.location.exits and self.location.exits[move_command] != None:
                self.location = self.location.exits[move_command]
            else:
                print('')
                print('That does not seem to be a viable exit from here.')
				
        print('')
        move_command = input('which direction? ')
        move_command = move_command.lower()
		
        if len(move_command) < 2 and move_command in move_alias_dict:
            move_command = move_alias_dict[move_command]
			
        execute_move(self, move_command)
		
# Instatiate rooms		
town_square = Room('Town Square')
general_store = Room('General Store')

# Declare room properties
town_square.description = "The central town square has a smattering of people going about their daily business."
town_square.exits = {
		    'north' : general_store,
		    'south' : None,
		    'east' : None,
		    'west' : None
        }
		
general_store.description = "This humble structure serves as the town's only shop."
general_store.exits = {
		    'north' : None,
		    'south' : town_square,
		    'east' : None,
		    'west' : None
        }
				
	
# Instantiate game and player
game = Game()
player = Player()
player.location = town_square

# Game loop
while (game.running == True):
    player.location.describe()
    player.move()
 




