from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from authentication.models import User
from authentication.forms import SignupForm, LoginForm

# Create your views here.
"""
view for regestering user
"""
def signup(request):
    # if user tries to signup by entering required fields
    if request.method == 'POST':
        # retrieve fields
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # check both password same or not
        if password == confirm_password:

            # check username already exists or not
            if User.objects.filter(username=username).exists():
                messages.error(request, 'User already exists!!!')
            
            # check email already exists or not
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists!!!')
            
            # save and log in user
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                login(request, user)
                return redirect('home')

        else:
            messages.error(request, 'Your password and confirm password not matching!!!')

    # load signup form       
    form = SignupForm()
    context = {'sign_up_form':form}

    return render(request, 'authentication/signup.html', context)


"""
view for authenticating user and log in page
"""
def authlogin(request):
    # if user tries to login by entering required fields
    if request.method == 'POST':
        # required fields
        email = request.POST['email']
        password = request.POST['password']

        # authenticate user
        user = authenticate(request, email=email, password=password)
        
        # if user is authenticated, than log in
        if user is not None:
            login(request, user)
            return redirect('home')
        
        #if user is not authenticated(ie. wrong email or password)
        else:
            messages.error(request, 'Invalid Email or Password!!!')

    # load login form
    form = LoginForm()
    context = {'login_form':form}

    return render(request, 'authentication/login.html', context)
    

"""
view for logging out user
"""
def authlogout(request):
    # request log out
    logout(request)
    messages.success(request, 'Logged out successfully!!')
    return redirect('home')