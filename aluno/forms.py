from django.forms import ModelForm
from django import forms
from .models import Aluno,Cidade


class CidadeForm(ModelForm):

    class Meta:
        model = Cidade
        fields = '__all__'
        widgets={
            'nome':  forms.TextInput(attrs={'class': 'form-control' }),
            'sigla_estado': forms.TextInput(attrs={'class': 'form-control' }),
        }

class AlunoForm(ModelForm):
 
    class Meta:
        model = Aluno
        fields = '__all__'
        widgets = {
            'nome_aluno' : forms.TextInput(attrs={'class': 'form-control' }),
            'endereco' : forms.TextInput(attrs={'class': 'form-control' }),
            'email' : forms.EmailInput(attrs={'class': 'form-control' }),
            'cidade': forms.Select(attrs={'class': 'form-control' }),
            'curso': forms.Select(attrs={'class': 'form-control' }),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
        }

