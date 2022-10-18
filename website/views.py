from django.shortcuts import render

# Create your views here.
def website(request):
    judul = []

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'indexwebsite.html', konteks)
