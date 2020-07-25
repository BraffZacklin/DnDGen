#!/bin/python
import rolls, magic, equipment, classes, races, attributes, levelling

class Character():
	def __init__(self, name, race, char_class, magic, equipment, level, stats):
		self.name = name
		self.race = race
		self.char_class = char_class
		self.magic = magic
		self.equipment = equipment
		self.level = level
		self.level_up_table = self.combine_levelling_tables()
		self.information = self.update_information()
		self.skills = self.update_skills(self.stats, self.proficiencies)

	def update_information(self):
		self.information = f'{self.name}, '
		self.information += f'level {self.level} '
		self.information += f'{self.race.name} '
		self.information += f'{self.char_class.name}\n'
		self.information += f'Magic: {self.list_magic()}\n'
		self.information += f'Equipment: \n{self.list_equipment()}'

	def print_information(self):
		self.update_information()
		print(self.information)

	def combine_levelling_tables(self):
		# Get race level table, class level table, subclass level table
		return ''

	def list_magic(self):
		return ''

	def list_equipment(self):
		return ''

	def print_levelling_tables(self):
		return ''

	def level_up(self):
		return ''

# char_class will also contain archetype
Percival = Character('Percival', races.human, classes.bard, 'PLACEHOLDER', 'PLACEHOLDER', 20, 'PLACEHOLDER')
Percival.char_class.Subclass(classes.college_of_glamour)
Percival.print_information()