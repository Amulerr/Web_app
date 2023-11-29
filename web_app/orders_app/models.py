from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy
from django.db import models
from datetime import datetime


class Employees(models.Model):
    """Сотрудник"""

    class Meta:
        db_table = "employee"
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    surname = models.TextField(verbose_name="Фамилия")
    name = models.TextField(verbose_name="Имя")
    middle_name=models.TextField(verbose_name="Отчество")
    email=models.TextField(verbose_name='Почта')

    def __str__(self):
        return f"{self.surname} {self.name}{self.middle_name}"


class Employment_history(models.Model):
    """История трудовой деятельности"""

    class Meta:
        db_table = "employment_history"
        verbose_name = "История трудовой деятельности"
        verbose_name_plural = "История трудовой деятельности"

    organisation = models.TextField(verbose_name="Наименование организации")
    employee = models.ForeignKey(Employees, on_delete=models.RESTRICT, verbose_name="Идентификатор сотрудника")
    reason = models.TextField(verbose_name="Причина увольнения")
    position= models.TextField(verbose_name="Занимаемая должность")

    def __str__(self):
        return f"{self.organisation} {self.employee}{self.reason}{self.position}"


class Business_trip(models.Model):
    """Командировки"""

    class Meta:
        db_table = "business_trip"
        verbose_name = "Командировка"
        verbose_name_plural = "Командировки"

    city = models.TextField(verbose_name='Город назначения')
    employee = models.ForeignKey(Employees, on_delete=models.RESTRICT, verbose_name="Идентификатор сотрудника")
    days = models.TextField(verbose_name='Количество дней')

    def __str__(self):
        return f"{self.city} {self.days}{self.employee}"



class Dismissal(models.Model):
    """Увольнение"""

    class Meta:
        db_table = "dismissal"
        verbose_name = "Увольнение"
        verbose_name_plural = "Увольнения"

    order= models.TextField(verbose_name="Приказ")
    employee = models.ForeignKey(Employees, on_delete=models.RESTRICT, verbose_name="Идентификатор сотрудника")
    date= models.TextField(verbose_name='Причина увольнения')

    def __str__(self):
        return f"{self.order} {self.date}{self.employee}"
    

    