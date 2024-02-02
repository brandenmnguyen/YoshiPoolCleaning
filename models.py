# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_username = models.CharField(unique=True, max_length=50, blank=True, null=True)
    admin_password = models.CharField(max_length=255, blank=True, null=True)
    admin_email = models.CharField(max_length=100, blank=True, null=True)
    admin_phone = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ADMIN'


class Appointments(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    cl = models.ForeignKey('Client', models.DO_NOTHING, blank=True, null=True)
    emp = models.ForeignKey('Employee', models.DO_NOTHING, blank=True, null=True)
    appdate = models.DateField(blank=True, null=True)
    apptime = models.TimeField(blank=True, null=True)
    admin_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APPOINTMENTS'


class Client(models.Model):
    client_id = models.AutoField(db_column='Client_id', primary_key=True)  # Field name made lowercase.
    fname = models.CharField(max_length=100, blank=True, null=True)
    lname = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(unique=True, max_length=100, blank=True, null=True)
    cl_password = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CLIENT'


class Company(models.Model):
    c_id = models.AutoField(db_column='C_id', primary_key=True)  # Field name made lowercase.
    company_name = models.CharField(db_column='Company_Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    company_address = models.CharField(db_column='Company_Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    company_phone = models.CharField(db_column='Company_Phone', max_length=15, blank=True, null=True)  # Field name made lowercase.
    company_email = models.CharField(db_column='Company_Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
    company_pw = models.CharField(db_column='Company_PW', max_length=255, blank=True, null=True)  # Field name made lowercase.
    admin = models.ForeignKey(Admin, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'COMPANY'


class Employee(models.Model):
    employee_id = models.AutoField(db_column='Employee_id', primary_key=True)  # Field name made lowercase.
    fname = models.CharField(max_length=50, blank=True, null=True)
    lname = models.CharField(max_length=50, blank=True, null=True)
    c = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True)
    emp_password = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_admin = models.IntegerField(blank=True, null=True)
    admin = models.ForeignKey(Admin, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EMPLOYEE'


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, models.DO_NOTHING, blank=True, null=True)
    emp = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True)
    received_date = models.DateField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payment_method = models.CharField(max_length=50, blank=True, null=True)
    card_name = models.CharField(max_length=100, blank=True, null=True)
    expdate = models.DateField(db_column='ExpDate', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=100, blank=True, null=True)
    reference_number = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    admin_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PAYMENT'


class Taskping(models.Model):
    task_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    taskname = models.CharField(db_column='taskName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    emp = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True)
    client = models.ForeignKey(Client, models.DO_NOTHING, blank=True, null=True)
    admin_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TASKPING'
