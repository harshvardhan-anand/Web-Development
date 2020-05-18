from django.shortcuts import render
from app.models import PersonDetails , Article
# Create your views here.
# In VS COde you will see a error "PersonDetail have has no object" is due to the pylint not due to django
def homepage(response):
    detail = PersonDetails.objects.all()
    print()
    print(detail[0].user_id)  # now this can be injected to html
    print(list(detail))
    print()
    return render(response, 'app/homepage.html')