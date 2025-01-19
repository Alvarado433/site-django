from django.db import models

class app(models.Model):
    """
        modelo que representa uma transação
    """
    nome = models.CharField(max_length=255, verbose_name="nome")
    idade = models.FloatField(verbose_name="idade")
    Date_nascimento = models.DateField(verbose_name="Date De nascimento")
    criado_em = models.DateField(auto_now_add=True, verbose_name= "data de criaçao")
    atualizado = models.DateTimeField(auto_now=True, verbose_name="data de edicao")

      
    def __str__(self):
        """
        retorna: str: o nome 
        """
        return self.nome
    
    class meta:
        verbose_name = 'teste'
        verbose_name_putal = 'teste'