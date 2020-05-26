from django.shortcuts import render
from . import form


# Create your views here.
def homepage(request):
    audiofile = form.FileUpload()
    if request.method == 'POST':
        filled_form = form.FileUpload(request.POST)
        uploaded_file = request.FILES
        print(uploaded_file)
    context = {'file_upload':audiofile}
    return render(request, 'homepage/homepage.html', context=context)

