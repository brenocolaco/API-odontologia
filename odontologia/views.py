from rest_framework import viewsets
from odontologia.models import ACD, Aluno
from odontologia.serializer import ACDSerializer, AlunoSerializer

# Create your views here.

class ACDsViewSet(viewsets.ModelViewSet):
    '''Exibindo todos os ACDs'''
    queryset = ACD.objects.all()
    serializer_class = ACDSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    '''Exibindo todos os alunos'''
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer