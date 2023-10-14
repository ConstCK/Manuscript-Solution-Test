from django import forms

from project.settings import BASE_DIR


class DBCreationForm(forms.Form):
    filename = forms.FilePathField(label="Введите имя файла xlsx", path=BASE_DIR)
    # filename = forms.FileField(label="Введите имя файла xlsx")
    sheet = forms.CharField(label="Введите имя листа xlsx")


class FileCreationForm(forms.Form):
    filename = forms.CharField(label="Введите имя файла")
