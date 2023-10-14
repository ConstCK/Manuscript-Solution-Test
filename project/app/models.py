from django.db import models


class COUNTRY(models.Model):
    ID_COUNTRY = models.IntegerField(primary_key=True)
    NAME_COUNTRY = models.CharField(max_length=64, unique=True, verbose_name="Страна")

    def __str__(self):
        return f"{self.NAME_COUNTRY}"

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"


class ISG(models.Model):
    ID_ISG = models.IntegerField(primary_key=True)
    NAME_ISG = models.CharField(max_length=512, verbose_name="Производитель")

    def __str__(self):
        return f"{self.NAME_ISG}"

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"


class GOODS(models.Model):
    ID_TOVAR = models.IntegerField(primary_key=True)
    NAME_TOVAR = models.CharField(max_length=512, verbose_name="Название товара")
    BARCOD = models.CharField(max_length=256, verbose_name="Штрихкод", null=True)
    ID_COUNTRY = models.ForeignKey("COUNTRY", on_delete=models.CASCADE, related_name="get_goods",
                                   verbose_name="Страна производитель")
    ID_ISG = models.ForeignKey("ISG", on_delete=models.CASCADE, related_name="get_goods",
                               verbose_name="Производитель товара")

    def __str__(self):
        return f"{self.NAME_TOVAR}"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
