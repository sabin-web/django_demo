from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from .models import EmployeeInfo
from .forms import EmployeeInfoModelForm
# Create your views here.



class MainView(View):
	def get(self,request):
		data = EmployeeInfo.objects.all()
		ctx = {
			'data':data
		}
		return render(request, 'myapp/employee_list.html', ctx)



class NewEmployeeInfo(View):
	template = 'myapp/create_employee.html'
	success_url = reverse_lazy('myapp:all')

	def get(self,request):
		form = EmployeeInfoModelForm()
		ctx = {'form':form}
		return render(request,self.template,ctx)

	def post(self,request):
		form = EmployeeInfoModelForm(request.POST)
		if not form.is_valid():
			ctx = {'form': form}
			return render(request, self.template, ctx)

		form.save()
		print(form.save())
		return redirect(self.success_url)



class UpdateEmployeeInfo(View):
	model = EmployeeInfo
	success_url = reverse_lazy('myapp:all')
	template = 'myapp/create_employee.html'

	def get(self,request,pk):
		make = get_object_or_404(self.model,pk=pk)
		form = EmployeeInfoModelForm(instance = make)
		ctx = {'form':form}
		return render(request, self.template, ctx)
	def post(self, request, pk):
		make = get_object_or_404(self.model, pk=pk)
		form = EmployeeInfoModelForm(request.POST, instance=make)
		if not form.is_valid():
			ctx = {'form': form}
			return render(request, self.template, ctx)

		form.save()
	
		return redirect(self.success_url)


class DeleteEmployeeInfo(View):
	model = EmployeeInfo
	success_url = reverse_lazy('myapp:all')
	template = 'myapp/make_confirm_delete.html'

	def get(self, request, pk):
		make = get_object_or_404(self.model, pk=pk)
		form = EmployeeInfoModelForm(instance=make)
		ctx = {'make': make}
		return render(request, self.template, ctx)

	def post(self, request, pk):
		make = get_object_or_404(self.model, pk=pk)
		make.delete()
		return redirect(self.success_url)


