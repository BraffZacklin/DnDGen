#!/bin/python
import levelling

class Race():
	def __init__(self, race, names, size, speed, level_up_table):
		self.name = race
		self.names = names
		self.size = size
		self.speed = speed
		self.level_up_table = level_up_table

# names = {'first' : ['list', 'of', 'first', 'names'], 'middle' : ['list', 'of', 'middle', 'names'], 'last' : ['list', 'of', 'last', 'names']
human_names = {'first' : ['Paul', 'Andy', 'Heather', 'Reginald', 'Percival'], 'middle' : ['James', 'Genine'], 'last' : ['Python']}

human = Race('Human', human_names, 'medium', 30, levelling.human)
dragonborn Race('Human', dragonborn_names, 'medium', 30, levelling.dragonborn)

races = [dragonborn, dwarf, elf, gnome, half_elf, half_orc, halfling, human, tiefling]