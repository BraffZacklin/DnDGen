#!/bin/python
from random import randint

class diceroll():
	def __init__(self, upper):
		self.lower = 1
		self.upper = upper

	def roll(self, factors=None):
		base_roll = randint(self.lower, self.upper)
		augment = self.consider_factors(factors)
		final_roll = base_roll + augment
		return (final_roll, base_roll)

	def consider_factors(self, factors):
		augment = 0		
		return augment

d2 = diceroll(2)
d4 = diceroll(4)
d6 = diceroll(6)
d8 = diceroll(8)
d10 = diceroll(10)
d12 = diceroll(12)
d20 = diceroll(20)