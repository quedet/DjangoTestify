from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['content']
        widgets = {
            'content': forms.TextInput(attrs={'class': 'flex-[10]'})
        }


class TodoCompleteForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['completed']