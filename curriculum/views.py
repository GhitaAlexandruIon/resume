from django.shortcuts import render


def index(request):
    return render(request, 'curriculum/index.html', {})


def about(request):
    return render(request, 'curriculum/about_page.html', {})



def awards(request):
    return render(request, 'curriculum/awards_page.html', {})


def education(request):
    return render(request, 'curriculum/education.html', {})


def experience(request):
    return render(request, 'curriculum/experience.html', {})


def interests(request):
    return render(request, 'curriculum/interests.html', {})


def skills(request):
    return render(request, 'curriculum/skills.html', {})
