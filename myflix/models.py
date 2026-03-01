from django.db import models

# Create your models here.


'''
Model
	id
	nome
	email
	cpf (max 11 caracteres)
	data de nascimento
	numero de telefone (max 14 caracteres)
'''

'''

'''

class user(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(blank= False, max_length=100)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    numero_telefone = models.CharField(max_length=14)

    def __str__(self):
        return self.nome

'''
    id
	codigo do streams (max 10car )
	descrição
	categoria (Filmes, Série e documentário)
'''

class stream(models.Model):
    codigo_stream = models.CharField(max_length=10)
    descricao = models.TextField(max_length=255, blank=False)
    categoria = models.CharField(max_length=1, choices=[('F', 'Filmes'),
    ('S', 'Série'), ('D', 'Documentário')], blank=False, default='F')

    def __str__(self):
        return self.codigo_stream
    
