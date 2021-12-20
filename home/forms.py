from django import forms
from .models import Profile, BlogPost

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_no', 'bio', 'facebook', 'instagram', 'linkedin', 'image', )
     
        
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'category', 'slug', 'content', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Titulo del Blog'}),
            'category':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Titulo de la Categoria'}),
            'slug': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Copie el título sin espacios y con un guión en el medio'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Insertar Contenido/informacion'}),
        } 
        labels = {
            'category' : 'Categoria',
            'title' : 'Título',
            'slug' : 'Enlace de redireccion',
            'content' : 'Contenido'
        }
        