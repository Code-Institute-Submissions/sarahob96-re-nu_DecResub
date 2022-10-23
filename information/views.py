from django.shortcuts import render

# Create your views here.

def contact(request):


    if request.method == 'POST':
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        message_fields = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        }   

    return render(request, 'information/contact.html')

def contact_success(request):

    return render(request, 'information/contact-success.html')