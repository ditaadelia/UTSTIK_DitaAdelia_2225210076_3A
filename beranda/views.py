from django.shortcuts import render

# Create your views here.
def beranda(request):
    judul = []

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'indexberanda.html', konteks)
