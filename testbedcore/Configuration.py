import configparser, sys
class Configuration():


	def __init__(self, configFile):
		self.config = configparser.RawConfigParser()
		self.config.read(configFile)

	def load(self):
		pass

	def getValue(self, section, key):
		value = None
		try:
			value = self.config.get(section, key)
		except:
			print(" Exception encountered getValue- " + sys.exc_info()[0])
		return value


