from django.shortcuts import render, redirect
from .forms import CGPAForm

def calculate(request):
    if request.method == 'POST':
        form = CGPAForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            marks = form.cleaned_data['marks']
            cgpa = float(marks) / 50
            
            request.session['student_name'] = name
            request.session['total_marks'] = float(marks)
            request.session['cgpa'] = round(cgpa, 2)
            
            return redirect('q3:result')
    else:
        form = CGPAForm()
    
    return render(request, 'q3/calculate.html', {'form': form})

def result(request):
    name = request.session.get('student_name', 'Student')
    marks = request.session.get('total_marks', 0)
    cgpa = request.session.get('cgpa', 0)
    
    return render(request, 'q3/result.html', {
        'name': name,
        'marks': marks,
        'cgpa': cgpa
    })
