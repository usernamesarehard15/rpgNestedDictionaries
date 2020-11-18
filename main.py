characters = {
	'John': {
		'description': 'just a regular accountant',
		'talent': 'math',
		'inventory': {
			'stapler': 'useful for binding paper',
			'ruler': 'great for drawing lines and measuring',
			'pencil': 'an essential item for office workers'
		}
	},
	'Harold': {
		'description': 'a pretty good chef',
		'talent': 'cooking',
		'inventory': {
			'cheese', 'a nice little snack',
			'knife', 'useful for more than cooking',
			'restaurant keys', 'only forgotten at home occasionally'
		}
	},
}

locations = {
	'the office': 'where John works and spends most of his time',
	'johns home': 'where John sleeps and spends most of his time outside of work',
	'papa harolds': 'a 5 star restaurant owned and operated by Harold',
	'harolds home': 'a regular house except every room has been turned into a kitchen'
}

# Print name, description and power for every character
for name, data in characters.items():
	print(f'{name} is {data["description"]}',
		f'{name} is good at {data["talent"]}', sep='\n')
print() # blank space

# Print name and description of locations
for location, desc in locations.items():
	print(f'{location.title()} is {desc}')
