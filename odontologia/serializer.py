from rest_framework import serializers
from odontologia.models import ACD, Aluno

class ACDSerializer(serializers.ModelSerializer):
    class Meta:
        model = ACD
        fields = '__all__'

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'