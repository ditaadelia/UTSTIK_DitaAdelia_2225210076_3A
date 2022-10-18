from django.shortcuts import render

# Create your views here.
def latihan(request):
    judul = []

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'indexlatihan.html', konteks)
