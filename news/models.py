from django.db import models

class Articles(models.Model): #класс Articles наследует все от класса Model
    title = models.CharField('Название',max_length=50)  
    anons = models.CharField('Анонс',max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}' #необходимо переадресовать пользователя на news/id


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новость'
#поля внутри таблицы. Нудно указать тип данных для этого поля.
# класс CharField - класс для строки. Первый аргумент - подпись для поля
# класс default - значение по умолчанию
# класс TextField - для больших объемов текста
# класс DateField - можно записать только дату
# класс DateTimeField -можно записать дату и время
# def str - для вывода на страницу названия статьи, а не ее id
# класс Meta - для вывода названия таблицы в панели администратор. verbose_name - ед.число. plural - мн.ч.
    
#МИГРАЦИИ-синхронизация нашего проекта с БД. Т.е. при создании таблицы внутри проекта,
# нужно ее содать и  в БД. 
# python manage.py makemigrations(создание файла миграций)
# python manage.py migrate - проведение миграций 
# Нужно не забыть зарегистрировать таблицу в файле admin.py
