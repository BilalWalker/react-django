from rest_framework import serializers
from leads.models import Lead

# Lead Serializer
# Creating lead serializer from lead model
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'