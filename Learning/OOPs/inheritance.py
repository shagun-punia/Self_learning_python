"""Simple example of class inheritance in Python with comments.

Run this file to see how a base class (Animal) is extended by
subclasses (Dog, Cat). Demonstrates method overriding and use of super().
"""

class Animal:
	"""Base class representing a generic animal."""

	def __init__(self, name, species):
		# initialize common attributes
		self.name = name
		self.species = species

	def speak(self):
		# A generic animal doesn't have a specific sound
		return "..."

	def info(self):
		# Return a simple description
		return f"{self.name} is a {self.species}."


class Dog(Animal):
	"""Dog inherits from Animal and overrides speak()."""

	def __init__(self, name, breed):
		# call the base class initializer using super()
		super().__init__(name, species="Dog")
		self.breed = breed

	def speak(self):
		# Dogs bark
		return "Woof!"

	def info(self):
		# Extend the base info with breed information
		base = super().info()
		return f"{base} Breed: {self.breed}."


class Cat(Animal):
	"""Cat inherits from Animal and overrides speak()."""

	def __init__(self, name, color):
		super().__init__(name, species="Cat")
		self.color = color

	def speak(self):
		# Cats meow
		return "Meow!"


if __name__ == "__main__":
	# create instances of the subclasses
	rover = Dog(name="Rover", breed="Labrador")
	whiskers = Cat(name="Whiskers", color="tabby")

	# demonstrate inherited and overridden behavior
	print(rover.info())        # inherited info() extended in Dog
	print(rover.speak())       # overridden speak()

	print(whiskers.info())     # uses Animal.info()
	print(whiskers.speak())    # overridden speak()

