from django.shortcuts import render, redirect
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            request.session['username'] = form.cleaned_data['username']
            request.session['email'] = form.cleaned_data['email']
            request.session['contact'] = form.cleaned_data['contact']
            return redirect('q1:success')
    else:
        form = RegisterForm()
    return render(request, 'q1/register.html', {'form': form})

def success(request):
    username = request.session.get('username', 'User')
    email = request.session.get('email', '')
    contact = request.session.get('contact', '')
    return render(request, 'q1/success.html', {
        'username': username,
        'email': email,
        'contact': contact
    })
