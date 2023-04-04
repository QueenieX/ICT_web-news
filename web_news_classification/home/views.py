from django.shortcuts import render
from django.contrib.auth.decorators import login_required
content = {
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
# Before accessing the below view
@login_required
def home(request):
    return render(request, 'home.html', content)

@login_required
def businessCategory(request):
    return render(request, 'business.html', content)

@login_required
def politicsCategory(request):
    return render(request, 'politics.html', content)

@login_required
def entertainmentCategory(request):
    return render(request, 'entertainment.html', content)

@login_required
def sportCategory(request):
    return render(request, 'sport.html', content)

@login_required
def techCategory(request):
    return render(request, 'tech.html', content)

# drop bar, serach bar do it in one page
# CSS
#