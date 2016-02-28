from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import PersonForm
from .models import Person


# Create your views here.
def index(request):
    if request.method == 'GET':
        people = Person.objects.all()
        context = {'people': people}
        return render(request, 'contacts/index.html', context)


def detail(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    context = {'person': person}
    return render(request, 'contacts/detail.html', context)


def create(request):
    form = PersonForm()

    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save()
        return HttpResponseRedirect(reverse(
            'contacts:detail', args=(person.id,)))

    return render(request, 'contacts/create.html', {'form': form})
