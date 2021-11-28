#Этот файл нужен для связи формы и модели Articles(таблицей в БД)
from .models import Articles
from django.forms import ModelForm, widgets, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title','anons','full_text', 'date']  #поля которые выводим в форму(из класса Articles (models))
        
        widgets={
            'title': TextInput(attrs={
                'class':'form-control',
                'placeholder':'Название статьи'
            }),
            'anons': TextInput(attrs={
                'class':'form-control',
                'placeholder':'Анонс статьи'
            }),
            'date': DateTimeInput(attrs={
                'class':'form-control',
                'placeholder':'Дата публикации'
            }),
            'full_text': Textarea(attrs={
                'class':'form-control',
                'placeholder':'Текст статьи'
            })
        }