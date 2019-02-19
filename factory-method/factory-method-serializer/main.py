import songs
import serializers
import yaml_serializer
song = songs.Song('1', 'Lavitate', 'Behemoth')
serializer = serializers.ObjectSerializer()

print(serializer.serialize(song, 'JSON'))
print(serializer.serialize(song, 'XML'))

# register new serializer
serializers.factory.register_format('YAML', yaml_serializer.YamlSerializer)
print(serializer.serialize(song, 'YAML'))