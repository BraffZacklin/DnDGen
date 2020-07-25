#!/bin/python
import rolls

class Stat():
	def __init__(self, name, value, proficiency):
		self.name = name
		self.value = value
		self.proficiency = proficiency

	def mod(self):
		return round(self.value / 2)

	def saving_throw(self):
		base_roll = rolls.diceroll(20)
		final_roll = base_roll + proficiency + mod()
		return final_roll

class Skill():
	def __init__(self, name, value, proficiency, associated_stat):
		self.name = name
		self.value = value
		self.proficiency = proficiency
		self.associated_stat = associated_stat

	def skill_check(self):
		if self.proficiency != None:
			base_roll = rolls.diceroll()