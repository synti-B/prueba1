from django import forms
from django.forms import fields
from .models import Comment, Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('__all__')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

class UsuarioLoginFormulario(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")

		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError("Este usuario No existe")
			if not user.check_password(password):
				raise forms.ValidationError("Incorrect Password")
			if not user.is_active:
				raise forms.ValidationError("Este Usuario No esta activo")

		return super(UsuarioLoginFormulario, self).clean(*args, **kwargs)

class RegistroFormulario(UserCreationForm):
	email = forms.EmailField(required=True)
	nombre = forms.CharField(required=True)
	apellido = forms.CharField(required=True)

	class Meta:
		model = User 

		fields = [
			'nombre',
			'apellido',
			'username',
			'email',
			'password1',
			'password2'
		]