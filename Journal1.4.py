class Animal:
	favorite_animal = "siberian tiger"
	arm_length: 91.0
	leg_length: 92.5
	eye_number: 2
	tail: True
	furry: True

	def __init__(self):
		self.name = favorite_animal
		self.arm = arm_length
		self.leg = leg_length
		self.eyes = eye_number
		self.tail = tail
		self.furry = furry

	def description(self):
		print(f"My favorite animal is the {self.name}. On average the {self.name} has arms that are approximately {self.arm} cm long," +
		f" while their legs are on average approximately {self.leg} cm long. They have {slef.eyes} eyes, it is {self.tail} they have a tail" +
		f" and it is also {self.furry} that they are furry.")