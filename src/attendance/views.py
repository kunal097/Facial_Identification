# for render HTMl pages
from django.shortcuts import render , redirect ,HttpResponse

# for defining view classes
from django.views import View
# for displaying form
from .forms import StudentForm , CalanderForm
# for storing the values in the database
from .models import Student,Calander
# for capture , training and identification
from recognizer_module import capture , train_recognizer_model , recognizer

# for tts
import os

# Create your views here.

# calss to show Home page
class IndexView(View):

	def get(self,request):
		return render(request , 'attendance/index.html',{})


# class to registering student

class RegisterView(View):

	# show the blank form on GET request
	def get(self,request):

		form = StudentForm()
		return render(request , "attendance/register.html" , {'form':form})

	# get the values of form on POST request
	def post(self,request):

		form = StudentForm(request.POST or None)


		if form.is_valid():

			name = form.cleaned_data['name']
			obj = form.save(commit=False)

			# save the object into database
			obj.save()

			# function to get user images 
			capture.Capture(obj.name,obj.stu_id)

			# function to train the recognizer model from the user images saved in images directory under recognizer_module
			train_recognizer_model.train()


			os.system("echo 'successfully registered '| festival --tts ")



			return render(request,'attendance/thank_you.html',{})
			
		return render(request,"attendance/register.html",{'form':form})	


# class to mark attendence using face identification
class MarkView(View):


	def get(self,request):

		# create info dictionary
		# i.e. -> {student_id : student_name }

		info={}

		data =Student.objects.all()

		for obj in data:
			info[obj.stu_id]=obj.name
		
		# call recognizer function
		# which take info and return id of detected face with confidence

		id_ , confd = recognizer.identify(info)

		# get complete details of the detected student
		obj = Student.objects.get(stu_id=id_)
		try:

			# check the status of the attendance of that student
			cal_obj = Calander.Objects.get(student=obj)

			
			
			
		except:

			# if the calander object is not created then create with the following details
			cal_obj = Calander()
			
			cal_obj.student = obj 
			cal_obj.status = 'P'
			cal_obj.save()


		os.system("echo 'attendance Marked'| festival --tts ")	

		return render(request , "attendance/thank_you.html" , {})






# class to check the status

class StatusView(View):

	def get(self,request):

		# info={}

		# data =Student.objects.all()

		# for obj in data:
		# 	info[obj.stu_id]=obj.name
	
		# id_ , confd = recognizer.identify(info)

		# try:
		# 	stu_obj = Student.objects.get(stu_id=id_)

		# 	print('***************************')
		# 	cal_obj = Calander.objects.get(student=stu_obj)
		# except:
		# 	# pass
		# 	print(id_)
		# 	return HttpResponse('Id not found')


		cal_obj = Calander.objects.all()


		return render(request , "attendance/status.html" , {'cal_obj':cal_obj})

			




		










