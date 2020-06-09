from django.shortcuts import render
import speech_recognition as sr

recogniser = sr.Recognizer()
def speech_recognition():
    with sr.Microphone() as source:
        # print('Google is listening')
        audio = recogniser.listen(source)
        # print('Recognizing')
        try:
            # There is requirement of internet connection
            text = recogniser.recognize_google(audio) # converting audio to text
            return (text)
        except Exception as e:
            print(e)
            return ("Google: There is Internet connectivity issue")

def homepage(request):
    if request.method == 'POST':
        text = speech_recognition()
        context = {'text':"You have said, {}.".format(text)}
    else:
        context = {'text':'Google: Please Say Something'}
    return render(request, 'homepage/homepage.html', context=context)