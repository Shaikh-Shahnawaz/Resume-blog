from django.shortcuts import render

# Create your views here.
def services(request):
    context = {'service':'active'}
    return render(request, 'servcs/services.html', context)