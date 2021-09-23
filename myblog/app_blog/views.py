from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'John Rening',
        'title': 'Deploying React Js Project on Google Firebase',
        'content': 'We will not spend time in writing React Redux app rather let me share with you a readymade redux-scaffold-project. Please grab your copy from github repository here. In case you want to test the application then please follow the Installation steps written in project Readme.',
        'date': 'November 09, 2020'
    },
]

# Create your views here.


def home(request):
    context = {'posts': Post.objects.all(), 'title': 'Latest Articles',
               'home_page_status': 'active'}
    return render(request, 'app_blog/home.html', context)


def about(request):
    context = {'title': 'About This Blog', 'about_page_status': 'active'}
    return render(request, 'app_blog/about.html', context)
