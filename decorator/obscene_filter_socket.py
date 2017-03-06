
class ObsceneFilterSocket():
	def __init__(self, socket):
		self.socket = socket
		self.obscene_words = ["faggot", "bastard", "cumshot", "slut", "poop"]

	def send(self, data):
		censored_data = self.censor_data(data)
		print("Sending {0} to {1}".format(censored_data, self.socket.getpeername()[0]))
		self.socket.send(bytes(censored_data, 'utf-8'))

	def close(self):
		self.socket.close()

	def censor_data(self, data):
		censored_data = []
		words = data.decode('utf-8').split()
		for word in words:
			if word.lower() in self.obscene_words:
				word = "****"
			censored_data.append(word)
		return ' '.join(censored_data)
