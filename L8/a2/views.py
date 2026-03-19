from django.shortcuts import render, redirect
from .forms import FeedbackForm

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            request.session['student_name'] = form.cleaned_data['student_name']
            request.session['gender'] = form.cleaned_data['gender']
            request.session['course'] = form.cleaned_data['course']
            request.session['suggestion'] = form.cleaned_data['suggestion']
            
            return redirect('a2:thank_you')
    else:
        form = FeedbackForm()
    
    return render(request, 'a2/feedback.html', {'form': form})

def thank_you(request):
    student_name = request.session.get('student_name', 'Student')
    return render(request, 'a2/thank_you.html', {
        'student_name': student_name
    })
