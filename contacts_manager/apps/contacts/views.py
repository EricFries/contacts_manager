from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import PersonForm, OrganizationForm
from .models import Person, Organization


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


def delete(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    person.delete()
    return HttpResponseRedirect(reverse('contacts:index'))


def edit(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            person = form.save()
            return HttpResponseRedirect(reverse(
                'contacts:detail', args=(person.id,)))
    else:
        form = PersonForm(instance=person)
    return render(request, 'contacts/edit.html', {
        'form': form,
        'person_id': person.id
        })


def detail_organization(request, organization_id):
    organization = get_object_or_404(Organization, pk=organization_id)
    people = organization.person_set.all()
    context = {
        'organization': organization,
        'people': people
        }
    return render(request, 'contacts/detail_organization.html', context)


def new_organization(request):
    form = OrganizationForm()
    if request.method == 'POST':
        form = OrganizationForm(request.POST)
        if form.is_valid():
            organization = form.save()
            return HttpResponseRedirect(reverse(
                'contacts:detail_organization', args=(organization.id,)))

    return render(request, 'contacts/new_organization.html', {'form': form})
