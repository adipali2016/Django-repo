#This is my personal file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name': "adi", 'place': "ujjain"}
    return render(request, 'index.html', params)

def form(request):
    return render(request, 'form.html')

def about(request):
    
    return render(request, 'about.html')    

def analyze(request):
    djtext = request.GET.get('text', 'default')
    analyzed_data = ""
    vowels = "aeiou"
    number=0
    for char in djtext.lower():
        if char not in vowels:
            analyzed_data = analyzed_data + char
        else:
            number+=1    
    params = {'text': analyzed_data, 'number': number}
    return render(request, 'analyze.html', params)

# HttpResponse takes html as input and renders it to the webpage. 