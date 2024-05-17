from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from receptionist.models import Consultation_details
from datetime import datetime
from receptionist.forms import ConsultationForm
from django.urls import reverse
from django.contrib import messages
from datetime import date
from Pharmacist import views
from Pharmacist.models import Medicine


# Create your views here.

@login_required
def doctor_homepage(request):
    return render(request, 'doctor_homepage.html')

@login_required
def consultation_details(request):
    user = request.user
    today = date.today()

    if user.Designation == 'Doctor':
        consultation_details =Consultation_details.objects.filter(doctor=user.first_name ,is_consulted=0)
        # consultation_details = Consultation_details.objects.filter(doctor=user.first_name)
        return render(request, 'patientlist.html', {'consultation_details': consultation_details})
    else:
        return HttpResponse("You are not authorized to view this page.")


@login_required
def consultation_history(request, op_number):
    consultation_history = Consultation_details.objects.filter(op_number=op_number).exclude(date=date.today())
    print(consultation_history)
    return render(request, 'consultation_history.html', {'consultation_history': consultation_history, 'op_number': op_number})


@login_required
def edit_prescription_tbl(request,op_number):
    today = date.today()
    pt = Consultation_details.objects.filter(op_number=op_number, date=today).first()
    pt.is_consulted='True'

    # pt=Consultation_details.objects.get(op_number=op_number)
    print(pt.doctor)
    return render(request,'consultation_page.html',{'data':pt})

@login_required
def consultation_page(request, op_number):
    today = date.today()
    pt = Consultation_details.objects.filter(op_number=op_number, date=today).first()

    # pt=Consultation_details.objects.get(op_number=op_number)
    print(pt.doctor)
    pt.is_consulted='True'
    pt.save
    form=ConsultationForm(request.POST,instance=pt)
    if form.is_valid():
        
        form.save()
        return HttpResponse("<script>window.alert('Successfully Updated !!!!');window.location.href='/ptlist/'</script>")
    else:
        print(form.errors)
        return HttpResponse("<script>window.alert('Error occured !!!!');window.location.href='/ptlist/'</script>")


@login_required
def result(request):
    return render(request, 'medicine_search.html')


@login_required
def search_result(request):
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            medicines = Medicine.objects.filter(Category=category)
            return render(request, 'med_results.html', {'medicines': medicines, 'category': category})
    return render(request, 'medicine_search.html')