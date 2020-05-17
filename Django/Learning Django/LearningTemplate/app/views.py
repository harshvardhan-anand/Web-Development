from django.shortcuts import render

# Create your views here.
def homepage(response):
    inserted_data = {
        "inserted_location":"homepage",
        "inserted_from":"app.views"
    }
    return render(response, "homepage.html", context=inserted_data)

def about(response):
    return render(response, "about.html")