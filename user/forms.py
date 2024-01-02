from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=10, widget=forms.PasswordInput)
    password_repeat = forms.CharField(max_length=10, widget=forms.PasswordInput)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)


    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password_report = cleaned_data.get('password_repeat')

        if password != password_report:
            raise forms.ValidationError('Пароли не совпадают!')

        return cleaned_data