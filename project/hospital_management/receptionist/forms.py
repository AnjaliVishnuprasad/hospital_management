from django import forms
from .models import PatientRegistration
from Coordinator.models import User
from receptionist.models import Consultation_details

class PatientRegistrationForm(forms.ModelForm):
    class Meta:
        model = PatientRegistration
        fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'gender', 'address', 'phone_number']





class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation_details
        fields = ['op_number', 'patient_name', 'date', 'symptoms', 'Diagnosis', 'prescription']
        widgets = {
            'symptoms': forms.Textarea(attrs={'rows': 3}),
            'Diagnosis': forms.Textarea(attrs={'rows': 3}),
            'prescription': forms.Textarea(attrs={'rows': 3}),
        }

#     def __init__(self, *args, **kwargs):
#         super(ConsultationForm, self).__init__(*args, **kwargs)
#         self.fields['doctor'].required = False
#  # Add other fields as needed
