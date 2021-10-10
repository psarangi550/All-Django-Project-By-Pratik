from django.db import models

# Create your models here.
class Chuck_Choice(models.Model):
    roles=[('animal', 'ANIMAL'), ('career', 'CAREER'), ('celebrity', 'CELEBRITY'), ('dev', 'DEV'), ('explicit', 'EXPLICIT'), ('fashion', 'FASHION'), ('food', 'FOOD'), ('history', 'HISTORY'), ('money', 'MONEY'), ('movie', 'MOVIE'), ('music', 'MUSIC'), ('political', 'POLITICAL'), ('religion', 'RELIGION'), ('science', 'SCIENCE'), ('sport', 'SPORT'), ('travel', 'TRAVEL')]
    category=models.CharField(max_length=10,choices=roles)

    def __str__(self):
        return self.category




