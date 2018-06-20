from django import forms 
from .models import Student , Calander


class StudentForm(forms.ModelForm):

	class Meta:
		model = Student 
		fields = "__all__"



class CalanderForm(forms.ModelForm):

	class Meta:
		model = Calander
		fields = [ "status"
		]