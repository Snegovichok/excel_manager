from django import forms
from django.contrib.auth.models import User
from .models import ExcelFile

class ExcelUploadForm(forms.ModelForm):
    class Meta:
        model = ExcelFile
        # Форма содержит только поле файла; название файла будет установлено автоматически.
        fields = ['file']

        # Добавляем стили для поля файла
        widgets = {
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class OrganizationCreationForm(forms.ModelForm):
    
    class Meta:
        model = User
        # Запрашиваем только логин, пароль и наименование организации (сохраняем в first_name)
        fields = ['username', 'password', 'first_name']
        labels = {
            'username': 'Логин',
            'password': 'Пароль',
            'first_name': 'Наименование организации',
        }

        # Добавляем стили для полей формы
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.is_staff = False
        user.is_superuser = False
        if commit:
            user.save()
        return user
