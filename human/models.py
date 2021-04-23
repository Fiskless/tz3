from django.db import models


class Human(models.Model):

    GENDER = [
        ('MAN', 'Man'),
        ('WOMAN', 'Woman')]

    avatar = models.ImageField('Аватар')
    first_name = models.CharField('Имя', max_length=20)
    second_name = models.CharField('Фамилия', max_length=20)
    age = models.PositiveSmallIntegerField('Возраст')
    gender = models.CharField(max_length=5, choices=GENDER)


    def __str__(self):
        return f'{self.first_name} {self.second_name}'

    class Meta:
        verbose_name = 'человек'
        verbose_name_plural = 'люди'
