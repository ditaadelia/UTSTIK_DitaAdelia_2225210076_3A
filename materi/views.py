from django.shortcuts import render

# Create your views here.
def materi(request):
    judul = []

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'indexmateri.html', konteks)
