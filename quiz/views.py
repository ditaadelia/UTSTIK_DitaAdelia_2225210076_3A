from django.shortcuts import render

# Create your views here.
def quiz(request):
    judul = []

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'indexquiz.html', konteks)
