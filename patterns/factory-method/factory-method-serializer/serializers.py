"""
Example from: https://realpython.com/factory-method-python/
Factory Method as an Object Factory
"""

import json
import xml.etree.ElementTree as et


class JsonSerializer:
	def __init__(self):
		self._current_object = None

	def start_object(self, object_name, object_id):
		self._current_object = {
			'id': object_id,
		}

	def add_property(self, name, value):
		self._current_object[name] = value

	def to_str(self):
		return json.dumps(self._current_object)


class XmlSerializer:
	def __init__(self):
		self._element = None

	def start_object(self, object_name, object_id):
		self._element = et.Element(object_name, attrib={'id': object_id})

	def add_property(self, name, value):
		prop = et.SubElement(self._element, name)
		prop.text = value

	def to_str(self):
		return et.tostring(self._element, encoding='unicode')\


class ObjectSerializer:
	def serialize(self, serializable, serialization_format):
		serializer = factory.get_serializer(serialization_format)
		serializable.serialize(serializer)
		return serializer.to_str()


# Support additional formats
class SerializerFactory:

	def __init__(self):
		self._creators = {}

	def register_format(self, serialization_format, creator):
		self._creators[serialization_format] = creator

	def get_serializer(self, serialization_format):
		creator = self._creators.get(serialization_format)
		if not creator:
			raise ValueError(serialization_format)
		return creator()


factory = SerializerFactory()
factory.register_format('JSON', JsonSerializer)
factory.register_format('XML', XmlSerializer)
print(factory._creators)