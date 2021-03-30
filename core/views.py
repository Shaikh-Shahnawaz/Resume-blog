from django.shortcuts import render, HttpResponse
from core.models import Contact
from django.contrib import messages
# Create your views here.
def home(request):
    context = {'home':'active'}
    return render(request, 'core/home.html',context)
    # return HttpResponse('this is home page')

def contact(request):
    if request.method == 'POST':

        nm = request.POST['name']
        em = request.POST['email']
        sb = request.POST['subject']
        msg = request.POST['message']
        contact = Contact(name=nm, email=em, subject=sb, message=msg) 
        contact.save()
        messages.success(request, 'Form Submitted Sucessfully!!')

        contact = Contact()

        
        
    
    context = {'contact':'active'}

    return render(request, 'core/contact.html', context)



#  if request.method == 'POST':
#         name = request.POST['name']
#         phone = request.POST['phone']
#         email = request.POST['email']
#         message = request.POST['message']

#         contact = Contact(name=name, phone=phone, email=email, message=message)
#         contact.save()
#     # showIndx = Contact.objects.all()
#     return render(request, 'myblog/index.html') 