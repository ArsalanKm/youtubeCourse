from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
    {
        'author': 'arsalan',
        'title': 'Blog post 1 ',
        'content': 'First post Content',
        'date_posted': 'Farvardin',

    },
    {
        'author': 'sahand',
        'title': 'Blog post 2',
        'content': 'Seceond  post Content',
        'date_posted': 'Shahrivar',

    }
]


def home(request):
    contest = {
        'posts': posts
    }
    return render(request, 'blog/home.html', contest)
    pass


def about(request):
    return render(request, 'blog/about.html',{'title':"About"})
