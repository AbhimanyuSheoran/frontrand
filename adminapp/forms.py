from django import forms
    
class UploadImageForm(forms.Form):
    image = forms.ImageField()
    caption = forms.CharField(max_length=100)
    
class UploadFaceForm(forms.Form):
    image = forms.ImageField()
    name = forms.CharField(max_length=255)
    detail= forms.CharField(max_length = 255)
    testimonial = forms.CharField(max_length = 300)