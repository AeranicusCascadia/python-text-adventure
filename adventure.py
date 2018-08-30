import textwrap

# Move list and alias dictionary
list_move_commands = ['north', 'south', 'east', 'west']
move_alias_dict = {
	'n' : 'north',
	's' : 'south',
	'e' : 'east',
	'w' : 'west',
	'u' : 'up',
	'd' : 'down',
	'go north' : 'north',
	'go south' : 'south',
	'go east' : 'east',
	'go west' : 'west',
	'go up' : 'up',
	'go down' : 'down',
	
	'go n' : 'north',
	'go s' : 'south',
	'go e' : 'east',
	'go w' : 'west',
	'go u' : 'up',
	'go d' : 'down'
}

# Classes
class Game:
	def __init__(self):
		self.running = True
		
	def quit(self):
		print('')
		print('Thanks for playing!')
		print('')
		input('Press "Enter" to quit.')
		quit()
		
	def show_commands(self):
		print('')
		print('Simple Commands:')
		print('----------------')
		print('<commands> : Show this list of game commands.')
		print('<quit> : Exits the game')
		print('<look> : Take a detailed look around the area.')
		print('')
		print('<north>, <south>, <east>, <west>, <up>, <down> : Move in this direction.')
		print('Can abbreviate <n>, <s>, <e>, <w>, <u>, <d>')
		print('')
		print('Extended Commands:')
		print('------------------')
		print('To interact with an object or creature, use two-word command.')
		print('[verb] + [single space] + [object]')
		print('')
		print('Examples:')
		print('"read sign"')
		print('"eat apple"')
		print('"move chair"')
		print('"attack clown"')
		
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
		self.items = []
	
	def describe(self):
		print('')
		print('=' * len(self.name))
		print(self.name)
		print('=' * len(self.name))
		print('')
		for line in textwrap.wrap(self.description, 80):
			print(line)
		
	def show_items(self):
		print('')
		print('At this location you notice:')
		print('----------------------------')
		for item in self.items:
			print(item.name)
		
	def show_exits(self):
		print('')	
		print('Exits from here:')
		print('----------------')
		for k, v in self.exits.items():
			if v == None:
				print(k + ':', 'none visible')
			else:
				print(k + ':', v.name)
				
	def big_look(self):
		self.describe()
		self.show_items()
		self.show_exits()
						
class Player:
	def __init__(self):
		self.location = None
		self.inventory = []

	# Player movement method	
	def move(self, move_command): # Outer method
	
		def execute_move(self, destination): # Inner method
			if destination in self.location.exits and self.location.exits[move_command] != None:
				self.location = self.location.exits[move_command]
			else:
				print('That does not seem to be a viable exit from here.')
				
		print('')

		if move_command in move_alias_dict:
			move_command = move_alias_dict[move_command]
			
		execute_move(self, move_command)
		
		player.location.describe()
	
	# General command input method 
	def get_command(self):
		print('')
		command = input('-- > What is your command? --> ')
		command = command.lower()
		if command in list_move_commands or command in move_alias_dict:
			self.move(command)
		elif command in universal_commands_dict:
			print('That appears to be a universal command!')
			universal_commands_dict[command]()
		else:
			try:
				(verb, target) = command.split(" ")
				print(verb)
				print(target)
			except:
				print('')
				print("I'm afraid that I don't understand that command.")
			
class Object:
	def __init__(self, name):
		self.name = name
		self.description = None
		self.takeable = False
		
	def describe(self):
		for line in textwrap.wrap(self.description, 80):
			print(line)

class Readable(Object):
	def __init__(self, name):
		self.name = name
		self.text = None
	
	def show_text(self):
		for line in textwrap.wrap(self.text, 80):
			print(line)
# Instantiate game and player
game = Game()
player = Player()
		
# Instantiate and build objects
sign = Readable('sign')
sign.description = "A rustic wooden road sign."
sign.text = "Welcome to Greenwood."
sign.actions = {
	'examine' : sign.describe,
	'read' : sign.show_text
}

big_rock = Object('big rock')
statue = Object('statue')
				
# Instatiate rooms		
town_square = Room('Town Square')
town_square.items = [sign, big_rock, statue]

general_store = Room('General Store')

# set player starting location
player.location = town_square

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

# Universal Commands Dictionary
universal_commands_dict = {
	"look" : player.location.big_look,
	"quit" : game.quit,
	"commands" : game.show_commands
}
		
# Starting code outside game loop for now
player.location.big_look()

# Game loop
while (game.running == True):
	player.get_command()





