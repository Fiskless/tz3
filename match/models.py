from django.db import models

# Create your models here.
class Match(models.Model):

    GENDER = [
        ('MAN', 'Man'),
        ('WOMAN', 'Woman')]

    first_name = models.CharField('Имя', max_length=20)
    second_name = models.CharField('Фамилия', max_length=20)
    age = models.PositiveSmallIntegerField('Возраст')
    gender = models.CharField(max_length=5, choices=GENDER)

    def __str__(self):
        return f'{self.first_name} {self.second_name}'

    class Meta:
        verbose_name = 'пара'
        verbose_name_plural = 'пары'