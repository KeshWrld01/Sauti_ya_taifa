from django.shortcuts import render, redirect
from .models import Victim

def say_names(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age') or None
        county = request.POST.get('county', '')
        status = request.POST.get('status')
        date_of_incident = request.POST.get('date_of_incident') or None
        how_it_happened = request.POST.get('how_it_happened')
        additional_info = request.POST.get('additional_info', '')
        photo = request.FILES.get('photo')

        Victim.objects.create(
            name=name,
            age=age,
            county=county,
            status=status,
            date_of_incident=date_of_incident,
            how_it_happened=how_it_happened,
            additional_info=additional_info,
            photo=photo,
            approval='pending',  # 👈 always starts as pending
        )

        return redirect('submission_received')  # 👈 go to thank you page

    victims = Victim.objects.filter(approval='approved').order_by('-submitted_at')
    return render(request, 'say_names/say_names.html', {
        'victims': victims,
        'breadcrumbs': [
            {'name': 'Say Their Names', 'url': None}
        ]
    })

def submission_received(request):
    return render(request, 'say_names/submission_received.html')