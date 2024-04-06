from django import forms
from books.models import Book


class BaseBookForm:
    def __init__(self):
        self.cleaned_data = None

    def clean_title(self):
        title = self.cleaned_data['title']
        title_found = Book.objects.filter(title=title).exists()
        if title_found and self.cleaned_data['title'] != title:
            raise forms.ValidationError('The title is already exist')
        elif len(title) < 3:
            raise forms.ValidationError('The title should be at least 3 characters')

        return title

    def clean_author(self):
        author = self.cleaned_data['author']
        if not author or len(author) < 3:
            raise forms.ValidationError('The author name should be at least 3 characters')

        return author

    def clean_pages(self):
        pages = self.cleaned_data['pages']
        if not pages or pages <= 0:
            raise forms.ValidationError('The number of pages should be a positive integer greater than zero')

        return pages

    def clean_price(self):
        price = self.cleaned_data['price']
        if not price or price <= 0:
            raise forms.ValidationError('The price should be a positive integer greater than zero')

        return price


class BookForm(forms.Form, BaseBookForm):
    title = forms.CharField(widget=forms.TextInput(), required=True, label='Title', max_length=100)
    author = forms.CharField(widget=forms.TextInput(), required=True, label='Author', max_length=100)
    pages = forms.IntegerField(widget=forms.NumberInput(), required=True, label='Pages')
    price = forms.IntegerField(widget=forms.NumberInput(), required=True, label='Price')
    image = forms.ImageField(widget=forms.FileInput(), required=False, label='Image')


class BookModelForm(forms.ModelForm, BaseBookForm):
    class Meta:
        model = Book
        fields = '__all__'

