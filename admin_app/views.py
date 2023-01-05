from django.shortcuts import render
from admin_app.models import Message

# Create your views here.
"""
view for display user messages to admin
"""
def user_messages(request):
    # retrieve messages from Message model in db order by latest messages
    messeges = Message.objects.order_by('-id')
      
    context = {
        # pass messages key that contains message data to user_messages.html page
        'messages': messeges 
    }

    return render(request, 'admin/user_messages.html', context)