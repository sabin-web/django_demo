from .models import EmployeeInfo
from django.forms import ModelForm


class EmployeeInfoModelForm(ModelForm):
	class Meta:
		model = EmployeeInfo
		fields = '__all__'


