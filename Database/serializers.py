from rest_framework import serializers
from Database.models import Data

class DataSerial(serializers.HyperlinkedModelSerializer):
    many=True
    class Meta:
        model = Data
        fields = ['_id', 'group', 'lat', 'lon', 'color', 'ang', 'radius']