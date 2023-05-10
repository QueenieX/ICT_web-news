from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Newsarticles, Categories
from datetime import date
from .machineLearning.prediction import predict
import csv
from pathlib import Path

# user need to login before access to home page
@login_required
def home(request):
    # with open(Path(__file__).with_name('test.csv'), encoding='utf-8',errors= 'surrogateescape') as f:
    #     next(f)
    #     reader = csv.reader(f)
    #     for row in reader:
    #         _, created = Newsarticles.objects.get_or_create(
    #         title = row[1],
    #         categoryid = Categories(row[2]),
    #         date = '2023-05-10',
    #         url = row[5],
    #         content = row[6],
    #                 )
    newsarticles = {
        'newsarticles' : Newsarticles.objects.filter(date = date.today()),
        'categories' : Categories.objects.all()}
        
    return render(request, 'home.html', newsarticles)

def search(request):
    news_url = request.GET.get('url')
    predict_news = predict(news_url)
    _, created = Newsarticles.objects.get_or_create(
            title = predict_news[0],
            categoryid = Categories((predict_news[1])),
            date = '2023-05-10',
            url = news_url,
            content = predict_news[2],
                    )
    content = {
        'newsarticles' : Newsarticles.objects.filter(date = date.today()),
        'categories' : Categories.objects.all(),
        'predict_news' : (predict_news[0],predict_news[1]),
    }
    return render(request, 'home.html', content)


