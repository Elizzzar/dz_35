from django.shortcuts import render
from app.models import Test_dz_35
# Create your views here.

def main_view(request):
    data = Test_dz_35.objects.all()
    context = {'data' : data}
    return render(request, 'main.html', context)