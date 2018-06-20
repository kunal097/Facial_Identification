from django.shortcuts import render , redirect 
from django.views import View
from .forms import StudentForm , CalanderForm
from .models import Student,Calander
from recognizer_module import capture , train_recognizer_model , recognizer

# Create your views here.


class IndexView(View):

	def get(self,request):
		return render(request , 'attendance/index.html',{})



class RegisterView(View):

	def get(self,request):

		form = StudentForm()
		return render(request , "attendance/register.html" , {'form':form})

	def post(self,request):

		form = StudentForm(request.POST or None)

		if form.is_valid():
			name = form.cleaned_data['name']
			obj = form.save(commit=False)

			obj.save()

			capture.Capture(obj.name,obj.stu_id)

			train_recognizer_model.train()

			return render(request,'attendance/thank_you.html',{})
			# return redirect('index')
		return render(request,"attendance/register.html",{'form':form})	


class MarkView(View):

	def get(self,request):

		info={}

		data =Student.objects.all()

		for obj in data:
			info[obj.stu_id]=obj.name
		print('*************************')
		print('*************************')
		print('*************************')
		print(info)	

		id_ , confd = recognizer.identify(info)

		try:
			print("###################################3***********************88")
			obj = Student.objects.get(stu_id=id_)
			try:
				cal_obj = Calander.Objects.get(student=obj)
			except:
				cal_obj = Calander()
				print("###################################3")
				cal_obj.student = obj 
				cal_obj.status = 'P'
				cal_obj.save()
		except Exception as e:
			print(e)	


		
		# form = CalanderForm()
		return render(request , "attendance/mark_attendance.html" , {})




class StatusView(View):

	def get(self,request):

		info={}

		data =Student.objects.all()

		for obj in data:
			info[obj.stu_id]=obj.name
	
		id_ , confd = recognizer.identify(info)


		










