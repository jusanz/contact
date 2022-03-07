from rest_framework import serializers

from . import models

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Contact
        fields = ['json']