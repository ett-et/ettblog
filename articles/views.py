from django.shortcuts import render

app_name="articles"

def articles(req):
    return render(req, "articles/articles.html")
