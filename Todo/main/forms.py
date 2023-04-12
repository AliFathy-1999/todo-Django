from django.forms import ModelForm , TextInput ,CheckboxInput,Select,Textarea
from .models import Todo,TodoTasks
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 
class todoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['name', 'isCompleted']
        widgets = {
            'name': TextInput(attrs={
                'class' : 'form-control',
                'style':'width:50em',
            }),
            'isCompleted': CheckboxInput(attrs={
                'style':'width:2em;height:2em;margin:2em;',
            })
        }
class todoTaskForm(ModelForm):
    class Meta:
        model = TodoTasks
        fields = ['name', 'isCompleted', 'description']
        widgets = {
            'name': TextInput(attrs={
                'class' : 'form-control',
                'style':'width:50em',
            }),
            'description': Textarea(attrs={
                'class' : 'form-control',
                'style':'width:50em',
            }),
            'isCompleted': CheckboxInput(attrs={
                'style':'width:2em;height:2em;margin:2em;',
            }),
        }

class UserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widget = {
            "username": TextInput(attrs={
                "color": "blue",
                "class": "form-control"
                }),
            "email": TextInput(attrs={
                "color": "blue",
                "class": "form-control"
                }),
        }