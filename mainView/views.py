from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from user.models import UserProfile

# Create your views here.
def mainView(request):
    return render(request, 'mainView/index.html')

@login_required(login_url='login')
def search_donors(request):
    blood_group = request.POST.get('blood_group')
    area = request.POST.get('area')

    donors = None
    if blood_group and area:
        donors = UserProfile.objects.filter(blood_group=blood_group, area__icontains=area)
    else:
        donors = UserProfile.objects.none()

    return render(request, 'mainView/search_results.html', {
        'donors': donors,
        'blood_group': blood_group,
        'area': area,
    })


def about(request):
    return render(request, 'mainView/about.html')

def contact(request):
    return render(request, 'mainView/contact.html')