#!/bin/python
# class.name = subclass + class
import levelling

class char_Class():
	def __init__(self, class_name, level_0, level_up_table, archetypes):
		self.name = class_name
		self.class_name = class_name
		self.level_0 = level_0
		self.level_up_table = level_up_table
		self.archetypes = archetypes

	def Subclass(self, subclass):
		self.subclass = subclass
		self.name = self.subclass.archetype_name.title() + ' ' + self.class_name.title()

class Archetype():
	def __init__(self, archetype_name, level_up_table):
		self.archetype_name = archetype_name
		self.level_up_table = level_up_table


college_of_glamour = Archetype('college of glamour', levelling.college_of_glamour)
bard_archetypes = college_of_glamour
bard = char_Class('bard', levelling.bard_start, levelling.bard, bard_archetypes)