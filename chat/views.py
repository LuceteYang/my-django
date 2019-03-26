from django.shortcuts import render

# Create your views here.
def room(request):
    context = {}
    return render(request, 'room.html', context)