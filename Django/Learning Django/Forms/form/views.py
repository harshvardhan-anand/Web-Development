from django.shortcuts import render
from . import form
# Create your views here.
def homepage(response):
    return render(response, 'homepage/homepage.html')

def form_data(response):
    form_elements = form.FormElements()
    print()
    # print(form_elements)  # this is html of form
    if response.method == 'POST':
        postdata = form.FormElements(response.POST)
        # print(postdata)  # This will print the html returned after clicking the submit button

        print(postdata.is_valid()) 
        # This will only be true when all the data are valid and in correct form (eg. email without .com is not accepted)

        # untill you check is_valid you cannot use .cleaned_data
        if postdata.is_valid():
            print(postdata.cleaned_data['name'])
            print(postdata.cleaned_data['botcatcher'])
        print()


    return render(response, 'form/form.htm', {'form_elements':form_elements})