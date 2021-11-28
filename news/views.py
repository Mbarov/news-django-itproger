from django.shortcuts import render, redirect #(redirect -  для переадресации после нажатия кнопки 'добавить')
from .models import Articles # импорт класса,который отвечает за нужную табличку
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView # DW -на основе этого класса можно создать страницу, которая будет изменяться, в зав-ти от url

def news_home(request):
    news = Articles.objects.order_by('-date') #objects.all() - вывод всех эл-в. 
    #objects.order_by('-date') - сортировака по title/-title/date/-date
    #objects.order_by('-date')[:2] - только две записи
    return render(request,'news/news_home.html', {'news':news})

class NewsDetailView(DetailView):
    model = Articles # указываем что работаем с моделью Articles
    template_name = 'news/details_view.html' #шаблон, который будет обрабатывать страничку
    context_object_name =  'article' #название ключа, по которому будем передавать запись внутрь шаблона

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    model = Articles
    template_name = 'news/news-delete.html'
    success_url = '/news/' #укаывает на какой url переадресовываем пользователя после удаления

def create(request):
    error = '' #создаем переменную для вывода ошибок
    if request.method == 'POST': #при нажатии на кнопку 'добавить' выполняется проверка
        form = ArticlesForm(request.POST)  #получаем все данные, которые ввел пользователь
        if form.is_valid(): #проверяем правильность заполненных форм
            form.save() #если они корректны, то сохраняем данные в БД
            return redirect('home') #после сохранения данных в БД, открывается главная страница
        else: #если они не корректны, то выводим сообщение об ошибке
            error = 'Форма была неверной'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)