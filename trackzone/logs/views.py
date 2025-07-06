from django.shortcuts import render, redirect
from .models import LogEntry

def show_form(request):
    if request.method == "POST":
        # take the value from the key word in the HTML form: name='weight' 'name' 'note'
        name = request.POST.get("name")
        weight = request.POST.get("weight")
        note = request.POST.get("note")
        # --> insert into model into database
        LogEntry.objects.create(name=name, weight=weight, note=note)
        return redirect("/add/")

        # New variable to fetch data

    log_datas = LogEntry.objects.order_by('-id')
    return render(request, 'logs/submit.html', {'log_datas': log_datas})
# Create your views here.
