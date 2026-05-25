from django.shortcuts import render

def school(request):
    return render(request, 'school/school.html', {
        'breadcrumbs': [
            {'name': 'Sauti School', 'url': None}
        ]
    })

def your_rights(request):
    return render(request, 'school/your_rights.html', {
        'breadcrumbs': [
            {'name': 'Sauti School', 'url': '/school/'},
            {'name': 'Your Rights', 'url': None}
        ]
    })

def constitution(request):
    return render(request, 'school/constitution.html', {
        'breadcrumbs': [
            {'name': 'Sauti School', 'url': '/school/'},
            {'name': 'Constitution 101', 'url': None}
        ]
    })

def philosophy(request):
    return render(request, 'school/philosophy.html', {
        'breadcrumbs': [
            {'name': 'Sauti School', 'url': '/school/'},
            {'name': 'Philosophy of Resistance', 'url': None}
        ]
    })