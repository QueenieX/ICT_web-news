from django.shortcuts import render

context = {
        'news_list' : [
    {
    'title' : 'News 1',
    'category' : 'Politics',
    'postdate' : '27/3/2023',
    },
    {'title' : 'News 2',
    'category' : 'Business',
    'postdate' : '27/3/2023'},{
    'title' : 'News 3',
    'category' : 'Entertainment',
    'postdate' : '27/3/2023',
    },{
    'title' : 'News 4',
    'category' : 'Sport',
    'postdate' : '27/3/2023',
    },{
    'title' : 'News 5',
    'category' : 'Tech',
    'postdate' : '27/3/2023',
    }
]
    }
# Create your views here.
def home(request):
    return render(request, 'home.html', context)

def businessCategory(request):
    return render(request, 'business.html', context)

def politicsCategory(request):
    return render(request, 'politics.html', context)

def entertainmentCategory(request):
    return render(request, 'entertainment.html', context)

def sportCategory(request):
    return render(request, 'sport.html', context)

def techCategory(request):
    return render(request, 'tech.html', context)