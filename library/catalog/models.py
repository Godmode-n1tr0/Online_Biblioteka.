from django.db import models
from django.db.models import TextField
from django.forms import CharField
from django.urls import reverse


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=20)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, )
    isbn = models.CharField('ISBN', max_length=13)
    text = models.TextField(help_text='Здесь вы можете ввести краткое описание вашей книги. >_<')
    genre = models.ManyToManyField('Genre', help_text='Введите жанры книги. >_<')

    # languege = models.ManyToManyField('Languege', help_text='Введите язык книги. >_<')
    def get_absolute_url(self):
        return reverse('book.detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=20, help_text='Впишите сюда жанр книги')

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=20, help_text='Впишите сюда фамилию.')
    last_name = models.CharField(max_length=20, help_text='Впишите сюда имя.')
    father_name = models.CharField(max_length=20, help_text='Впишите сюда отчество.')
    date_of_birth = models.DateField(help_text='Впишите сюда свою дату рождения.', null=True)
    date_of_death = models.DateField(help_text='Впишите сюда дату сметри человека.')

    def get_absolute_url(self):
        return reverse('author.detail', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)

# class Language(models.Model):
#     name = models.CharField(max_length=20, help_text='Впишите сюда язык книги')
#
# def __str__(self):
#     return self.name
