from django.db import models

# Create your models here.
class Computer(models.Model):
    title = models.CharField(verbose_name='Название', max_length=50)
    build_date = models.DateTimeField(verbose_name='Дата сборки', auto_now_add=True, blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)

    id_pc = models.IntegerField(verbose_name='Номер ПК', unique=True)
    image = models.ImageField(upload_to='images', verbose_name='Изображение', blank=True)

    builder = models.ForeignKey('Builder', verbose_name='Сборщик', related_name='computers', null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Компьютер'
        verbose_name_plural = 'Компьютеры'
        ordering = ['id']

    def __str__(self):
        return self.title

class Builder(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=100)
    surname = models.CharField(verbose_name='Фамилия', max_length=100)
    patronymic = models.CharField(verbose_name='Отчество', max_length=100)
    builders = (('Начинающий', 'Начинающий'),('Опытный', 'Опытный'),('Называй меня - мастер', 'Называй меня - мастер'))
    level_of_competence = models.CharField(verbose_name='Звание', max_length=100, choices=builders, default="")

    class Meta:
        verbose_name = 'Сборщик'
        verbose_name_plural = 'Сборщики'
        ordering = ['first_name']

    def __str__(self):
        return f'{self.first_name} {self.surname} {self.patronymic}'

class CPU(models.Model):
    CPU_model = models.CharField(verbose_name='Процессор', max_length=50)
    computers = models.ManyToManyField(Computer, verbose_name='Компьютеры', related_name='CPUs')

    class Meta:
        verbose_name = 'Процессор'
        verbose_name_plural = 'Процессоры'
        ordering = ['CPU_model']

    def __str__(self):
        return self.CPU_model



class GPU(models.Model):
    GPU_model = models.CharField(verbose_name='Видеокарта', max_length=200, blank=True)
    computers = models.ManyToManyField(Computer, verbose_name='Компьютеры', related_name='GPUs')

    class Meta:
        verbose_name = 'Видеокарта'
        verbose_name_plural = 'Видеокарты'
        ordering = ['GPU_model']

    def __str__(self):
        return self.GPU_model


class Storage(models.Model):
    amount = models.PositiveIntegerField('Количество')
    price = models.PositiveIntegerField('Цена')
    computer = models.OneToOneField(Computer, related_name='storage', blank=True, null=True, verbose_name='Компьютер', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'
        ordering = ['amount', 'price']

    def __str__(self):
        return f'{self.computer} - {self.price}'

    def get_discount(self):
        return self.price - (self.price * 0.1)