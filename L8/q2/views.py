from django.shortcuts import render, redirect
from django.http import JsonResponse

# Store votes in session
def vote(request):
    if request.method == 'POST':
        choice = request.POST.get('choice')
        if choice in ['good', 'satisfactory', 'bad']:
            votes = request.session.get('votes', {'good': 0, 'satisfactory': 0, 'bad': 0})
            votes[choice] = votes.get(choice, 0) + 1
            request.session['votes'] = votes
            return redirect('q2:results')
    
    return render(request, 'q2/vote.html')

def results(request):
    votes = request.session.get('votes', {'good': 0, 'satisfactory': 0, 'bad': 0})
    total = sum(votes.values())
    
    if total > 0:
        good_percent = (votes['good'] / total) * 100
        satisfactory_percent = (votes['satisfactory'] / total) * 100
        bad_percent = (votes['bad'] / total) * 100
    else:
        good_percent = satisfactory_percent = bad_percent = 0
    
    return render(request, 'q2/results.html', {
        'good_votes': votes['good'],
        'satisfactory_votes': votes['satisfactory'],
        'bad_votes': votes['bad'],
        'good_percent': round(good_percent, 2),
        'satisfactory_percent': round(satisfactory_percent, 2),
        'bad_percent': round(bad_percent, 2),
        'total': total
    })
