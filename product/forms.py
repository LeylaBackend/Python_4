from django import forms

class ProductForm(forms.Form):
    image = forms.ImageField(
        required=False,
        label='Картинка',
    )
    title = forms.CharField(
        max_length=250,
        label='Назание поста',
    )
    text = forms.CharField(
        widget=forms.Textarea,
        label='Текст поста'
    )
    price = forms.IntegerField(
        label='Цена'
    )

class CategoryForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        label='Категория поста',
    )

class ReviewForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea,
        label='Ответ для поста'
    )


