from django.shortcuts import render

#функция index/about/news принимает 2 аргумента - запрос (request) и адрес шаблона html и может принять
# третий - данные, которые передаются через словарь. Далее в html нужно в двойных скобках{{}} написать ключ без кавычек
#при многоуровневом словаре обращение к самому нижнему элементу без кавычек - {{obj.car}}
#в html можно исп-ть конструкцию {% if el == 'abc' %} {{el}} {% endif %}
# {% filter upper %} {% endfilter %} - для верхнего или нижнего регистра
def index(request):
    data = {
        'title':'Главная',
        'values':['Some','Hello','123'],
        'obj':{
            'car':'bmw',
            'age':18,
            'hobby':'football'
        }
    }
    return render(request,'main/index.html', data) 

#в html для вывода какого либо элемента словаря через шаблонизатор jinja    :
# {% for el in values %}
# <p>{{el}}</p>
# {% endfor %}
# {{el|upper}} - краткая запись для одного элемента

def about(request):
    return render(request,'main/about.html')


def news(request):
    return render(request, 'main/news.html')
