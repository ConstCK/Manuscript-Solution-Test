import os
import csv

from django.db import IntegrityError
from django.db.models import Count
from django.shortcuts import render, redirect
from openpyxl import load_workbook

from django.http import HttpResponse

from .forms import DBCreationForm, FileCreationForm
from .models import GOODS, COUNTRY, ISG
from project.settings import BASE_DIR


def data_in(request):
    if request.method == "POST":
        form = DBCreationForm(request.POST)
        filename = form["filename"].data
        sheet_name = form["sheet"].data

        try:
            wb = load_workbook(filename=filename)
        except FileNotFoundError as err:
            print(err)
            return HttpResponse('Неверно указано имя файла')

        # Создание списков промежуточных данных для переноса их в БД
        id_tovar_range = wb[sheet_name]["A"]
        goods_range = wb[sheet_name]["B"]
        id_isg_range = wb[sheet_name]["C"]
        barcod_range = wb[sheet_name]["F"]
        isg_range = wb[sheet_name]["D"]
        country_range = wb[sheet_name]["E"]

        id_tovar_list = list()
        goods_list = list()
        id_isg_list = list()
        barcod_list = list()
        isg_list = list()
        country_list = list()

        for n, i in enumerate(id_tovar_range):
            if n == 0:
                continue
            id_tovar_list.append(i.value)

        for n, i in enumerate(goods_range):
            if n == 0:
                continue
            goods_list.append(i.value)

        for n, i in enumerate(id_isg_range):
            if n == 0:
                continue
            id_isg_list.append(i.value)

        for n, i in enumerate(barcod_range):
            if n == 0:
                continue
            barcod_list.append(i.value)

        for n, i in enumerate(isg_range):
            if n == 0:
                continue
            isg_list.append(i.value)

        for n, i in enumerate(country_range):
            if n == 0:
                continue
            country_list.append(i.value)

        # Заполнение таблицы стран
        for n, i in enumerate(set(country_list)):
            try:
                COUNTRY.objects.create(ID_COUNTRY=n, NAME_COUNTRY=i)
            except IntegrityError as err:
                print(err)
                continue

        # Заполнение таблицы производителей
        for i in range(1, len(isg_list)):
            try:
                ISG.objects.create(ID_ISG=id_isg_list[i], NAME_ISG=isg_list[i])
            except IntegrityError as err:
                print(err)
                continue

        # Заполнение таблицы товаров
        for i in range(len(goods_list)):
            try:
                country = COUNTRY.objects.get(NAME_COUNTRY=country_list[i])
                isg = ISG.objects.get(ID_ISG=id_isg_list[i])
            except Exception as err:
                print(err)
                return redirect("/error_page/")

            try:
                obj = GOODS(ID_TOVAR=id_tovar_list[i], NAME_TOVAR=goods_list[i], BARCOD=barcod_list[i],
                            ID_COUNTRY=country, ID_ISG=isg)
                obj.save()
            except Exception as err:
                print(err)
                return redirect("/error_page/")

        return redirect('/data_in_success/')

    else:
        form = DBCreationForm()
    return render(request, "data_in.html", {"form": form})


def data_out(request):
    if request.method == "POST":
        form = FileCreationForm(request.POST)
        filename = form["filename"].data

        countries = COUNTRY.objects.all().annotate(number=Count("get_goods")).order_by("-number")
        result = []
        for i in countries:
            result.append((i.NAME_COUNTRY, "-", i.number))

        file = os.path.join(BASE_DIR, filename)
        with open(file, "w") as f:
            writer = csv.writer(f, delimiter=" ")
            writer.writerows(result)
        return redirect("/data_out_success/")

    else:
        form = FileCreationForm()
    return render(request, "data_out.html", {"form": form})


def data_in_success(request):
    return render(request, "data_in_success.html")


def data_out_success(request):
    return render(request, "data_out_success.html")


def error_page(request):
    return render(request, "error_page.html")
