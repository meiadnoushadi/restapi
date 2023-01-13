from rest_framework import serializers
from .models import Openstack

class OpenstackSerializer(serializers.ModelSerializer):
    class Meta:
        model=Openstack
        fields='__all__'