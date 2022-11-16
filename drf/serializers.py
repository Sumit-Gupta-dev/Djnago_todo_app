from rest_framework import serializers
from todoapp.models import *

class taskSerializers(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = '__all__'