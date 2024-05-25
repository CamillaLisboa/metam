from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Person, Bill
from django.urls import reverse_lazy
from django.views.generic import ListView

# Create your views here.
class PersonIndex(ListView):
    model = Person
    template_name = 'person.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['person'] = self.get_person()
        return context

    def get_person(self):
        # Obtém as coordenadas dos alvos
        people = Person.objects.all()
        person_data = []

        for person in people:
            person_data.append({
                'name': person.name,
                'doc': person.doc,
                'income': person.income,
            })

        return person_data
    
class BillIndex(ListView):
    model = Bill
    template_name = 'bills.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bill'] = self.get_bill()
        return context

    def get_bill(self):
        # Obtém as coordenadas dos alvos
        bills = Bill.objects.all()
        bill_data = []

        for bill in bills:
            bill_data.append({
                'name': bill.name,
                'price': bill.price,
                'due_date': bill.due_date,
            })

        return bill_data