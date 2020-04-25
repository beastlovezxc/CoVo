'''
@Author: BeanCB
'''
from django.shortcuts import render
from .models import Helper
# Create your views here.
def get_helperlist(request):
    context = {}
    context['helperlist'] = Helper.objects.all().values('helper_number', 'helper_name')
    return render(request, './Helper/helperlist.html', context)

def get_helperinfo(request, helper_number):
    context = {}
    context['helperinfo'] = Helper.objects.get(helper_number = helper_number)
    return render(request, './Helper/helperinfo.html', context)