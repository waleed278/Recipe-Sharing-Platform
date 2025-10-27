from django import forms
from .models import Recipe
from django.core.validators import MinLengthValidator,MaxLengthValidator
from django.core.exceptions import ValidationError
from ckeditor.widgets import  CKEditorWidget

def no_numbers(value):
    if any (char.isdigit() for char in value):
       raise ValidationError('Name cannot contain numbers')
def validate_image_size(image):
    max_size_kb = 2048
    if image.size > max_size_kb * 1024:
        raise ValidationError("Image size should not exceed 2 MB.")

class RecipeForm(forms.ModelForm):
    def clean_recipe_name(self):
        name = self.cleaned_data.get('recipe_name')
        if len(name)<5:
            raise ValidationError("Name must be at least 5 characters long")
        return name
    
    def clean(self):
        cleaned_data =  super().clean()
        name = cleaned_data.get('recipe_name')
        des = cleaned_data.get('recipe_des')
        if name == des:
            raise ValidationError("Description Cant contain recipe name")
    
    recipe_name = forms.CharField(
    
    validators= [MaxLengthValidator(50),no_numbers]
    )
    recipe_des = forms.CharField(widget = CKEditorWidget())
    recipe_image = forms.ImageField(
        validators=[validate_image_size],
        widget=forms.ClearableFileInput(attrs={'class':'form-control'})
    )
    
    class Meta:
        model = Recipe
        fields = ['recipe_name', 'recipe_des', 'recipe_image']

widgets = {
    'recipe_name':forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder' : 'Enter Recipe Name'
    }),
    
    
    'recipe_image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
}