from django.shortcuts import render
from django.forms import Form, CharField
from django.http import HttpResponse

# Create your views here.

class TestForm(Form):
    name = CharField()

def django_hide_form_view(request):
    form = TestForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            return HttpResponse('Form is valid', status=200)
        else:
            return HttpResponse('Form is not valid', status=400)
    return render(request, 'django_hide_form.html', {'form': form})