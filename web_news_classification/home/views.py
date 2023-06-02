from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Newsarticles, Categories
from datetime import date
from .machineLearning.prediction import predict
from .extraction.getDailyUrls import *


news_title = []
# user need to login before access to home page
@login_required
def home(request):
    newsarticles = {
        'newsarticles' : Newsarticles.objects.filter(date = date.today()),
        'categories' : Categories.objects.all()}
        
    return render(request, 'home.html', newsarticles)

def search(request):
    today = date.today()
    try:
        news_url = request.GET.get('url')
        predict_news = predict(news_url)
        if (Newsarticles.objects.filter(title = predict_news[0]) == False):
            _, created = Newsarticles.objects.get_or_create(
                    title = predict_news[0],
                    categoryid = Categories(getcategoryid(predict_news[1])),
                    date = today,
                    url = news_url,
                    content = (predict_news[2])[:5000],
                            )
            
    except:
        predict_news = ['Error', 'please check your URL again']
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
        
def get_daily_news(reqeust):
    output = get_daily_urls()
    today = date.today()
    for url in output:
        predict_news = predict(url)
        if not Newsarticles.objects.filter(title = predict_news[0]).exists():
            try:
                _, created = Newsarticles.objects.get_or_create(
                    title = predict_news[0],
                    categoryid = Categories(getcategoryid(predict_news[1])),
                    date = today,
                    url = url,
                    content = (predict_news[2])[:5000],
                            )
            except:
                print('error')
    return HttpResponse("<html><script>window.location.replace('/home');</script></html>")

