from django.contrib import admin
from odontologia.models import ACD, Aluno

# Register your models here.

class ACDs(admin.ModelAdmin):
    list_display = ('id', 'nome', 'matricula')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'matricula')
    list_per_page = 10

#primeiro parametro é o modelo e segundo a configuração admin
admin.site.register(ACD, ACDs)

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    
#primeiro parametro é o modelo e segundo a configuração admin
admin.site.register(Aluno, Alunos)