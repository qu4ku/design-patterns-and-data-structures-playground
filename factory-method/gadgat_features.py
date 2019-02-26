# https://www.pythonprogramming.in/python/factory-method-implementation/

from abc import ABCMeta, abstractclassmethod


class Feature(metaclass=ABCMeta):
	@abstractclassmethod
	def specifications(self):
		pass


class DisplayFeatures(Feature):
	def specifications(self):
		print('5.5 inch, 1280x720px, TFT LCD IPS')


class ProcessorFeatures(Feature):
	def specifications(self):
		print('Mediatek MTK6737 1.3GHz, Quad Core, 1.3 GHz')


class StorageFeatures(Feature):
	def specifications(self):
		print('Internal Storage 32GB, RAM 3GB')


class CallFeatures(Feature):
    def specifications(self):
        print('Voice Call, Phonebook')


class Gadgets(metaclass=ABCMeta):
	def __init__(self):
		self.features = []
		self.feature_list()

	@abstractclassmethod
	def feature_list(self):
		pass

	def get_features(self):
		return self.features

	def add_feature(self, feature):
		self.features.append(feature)


class Mobile(Gadgets):
	def feature_list(self):
		self.add_feature(DisplayFeatures())
		self.add_feature(ProcessorFeatures())
		self.add_feature(CallFeatures())
		self.add_feature(StorageFeatures())


class Tablet(Gadgets):
	def feature_list(self):
		self.add_feature(DisplayFeatures())
		self.add_feature(StorageFeatures())
		self.add_feature(ProcessorFeatures())


def main():
	print('#### MOBILE FEATURE LIST ####')
	gadget1 = Mobile()
	for x in gadget1.get_features():
		x.specifications()

	print()
	print('#### TABLET FEATURE LIST ####')
	gadget2 = Tablet()
	for y in gadget2.get_features():
		y.specifications()

if __name__ == '__main__':
	main()