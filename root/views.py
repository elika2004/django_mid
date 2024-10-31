from django.shortcuts import render
from .models import Services , Prices , Pros , Testimonials , FQA , Services_two , Services , User 

# Create your views here.


def home(request):
    services=Services.objects.filter(status=True)
    return render(request, 'root/index.html',context={"services":Services})
    services=Services.objects.filter(status=True)
    services_two=Services_two.objects.filter(status=True)
    pros=Pros.objects.filter(status=True)
    prices=Prices.objects.filter(status=True)
    pros=Pros.objects.filter(status=True)
    user=User.objects.filter(status=True)
    fqa=FQA.objects.all()
    testimonials=Testimonials.objects.filter(status=True)
    context={
        'services':services,
        'services_tow':services_two,
        'pros':Pros,
        'prices':Prices,
        'testimonials':Testimonials,
        'fqa':FQA,

    }

    return render(request , 'root/index.html', context=context)
        
        




