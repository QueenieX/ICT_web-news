from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Newsarticles, Categories
from datetime import date
from .machineLearning.prediction import predict


# user need to login before access to home page
@login_required
def home(request):
    newsarticles = {
        'newsarticles' : Newsarticles.objects.filter(date = date.today()),
        'categories' : Categories.objects.all()}
        
    return render(request, 'home.html', newsarticles)

def search(request):
    news_url = request.GET.get('url')
    predict_news = predict(news_url)
    _, created = Newsarticles.objects.get_or_create(
            title = predict_news[0],
            categoryid = Categories(getcategoryid(predict_news[1])),
            date = '2023-05-17',
            url = news_url,
            content = predict_news[2],
                    )
    content = {
        'newsarticles' : Newsarticles.objects.filter(date = date.today()),
        'categories' : Categories.objects.all(),
        'predict_news' : (predict_news[0],predict_news[1]),
    }
    return render(request, 'home.html', content)

def getcategoryid(categoryname):
    for c in Categories.objects.all():
        if c.categoryname == categoryname:
            return c.categoryid
