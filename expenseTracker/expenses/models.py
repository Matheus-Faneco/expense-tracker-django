from django.db import models
from django.conf import settings


#Modelo de despesa
class Expense(models.Model):

    #Chave estrangeira de usuario
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        db_column='id_user',
        null=False,
        verbose_name='Usuario',
    )

    #O tipo de despesa será fixa
    CATEGORY_CHOICES = [
        ('groceries', 'Alimentação'),
        ('leisure', 'Lazer'),
        ('electronics', 'Eletrônicos'),
        ('utilities', 'Contas'),
        ('clothing', 'Roupas'),
        ('health', 'Saúde'),
        ('others', 'Outros'),
    ]
    #Titulo de despesa
    title = models.CharField(
        db_column='tx_title',
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Titulo',
    )
    #Valor de despesa
    amount = models.DecimalField(
        db_column='nb_amount',
        max_digits=10,
        decimal_places=2,
        null=False,
        verbose_name='Valor',
    )
    #Descrição de despesa
    description = models.CharField(
        db_column='tx_description',
        max_length=100,
        blank=True,
        verbose_name='Descrição',
    )
    #Data da despesa
    date = models.DateField(
        db_column='dt_date',
        null=False,
        verbose_name='Data',
    )
    #Tipo/Categoria de despesa
    category = models.CharField(
        db_column='tx_category',
        max_length=20,
        choices=CATEGORY_CHOICES,
        null=False,
        verbose_name='Categoria',
    )

    def __str__(self):
        return f'{self.user} - {self.title} - {self.amount}'


