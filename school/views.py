from django.shortcuts import render

def school(request):
    return render(request, 'school/school.html')

def your_rights(request):
    return render(request, 'school/your_rights.html')

def constitution(request):
    return render(request, 'school/constitution.html')

def philosophy(request):
    return render(request, 'school/philosophy.html')