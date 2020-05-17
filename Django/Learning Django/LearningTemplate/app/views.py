from django.shortcuts import render

# Create your views here.
def homepage(response):
    inserted_data = {
        "inserted_to":"I am inserted to homepage.html",
        "inserted_from":"I am inserted from app.views"
    }
    return render(response, "app/homepage.html", context=inserted_data)

def about(response):
    return render(response, "app/about.html")