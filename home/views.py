from django.shortcuts import render
from admin_app.models import Message
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
"""
view for home page
"""
def home(request):
    
    return render(request, 'home/home.html')

"""
view for about us page
"""
def about(request):
    
    return render(request, 'home/about.html')

"""
view for contact us page
"""
def contact(request):
    # if user tries to send message to admin
    if request.method == 'POST':
        # retrieve fields
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # save messages in Message model
        contactformdata = Message(name=name, email=email, subject=subject, message=message)
        contactformdata.save()
        messages.success(request, 'Message sent successfully!!!')

        # send user massage to admin by email
        send_mail("MyDictionary user message",
            f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}",
            f"{email}",
            ["reddibentur@gmail.com"])
    return render(request, 'home/contact.html')