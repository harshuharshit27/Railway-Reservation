from django import forms

from booking.models import Ticket, Route, RoutePath, Ticket


class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ('first_name', 'last_name', 'gender', 'user_name', 'age')
