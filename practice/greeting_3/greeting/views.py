from django.shortcuts import render
from .forms import NameForm


def index(request):
    greeting_name = None

    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            user = form.save()
            greeting_name = user.name
            form = NameForm()
    else:
        form = NameForm()

    return render(request, 'greeting/index.html', {
        'form': form,
        'greeting_name': greeting_name,
    })