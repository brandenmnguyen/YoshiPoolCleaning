from django.db import models
class Appointments(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    cl = models.ForeignKey('Client', models.DO_NOTHING, blank=True, null=True)
    emp = models.ForeignKey('Employee', models.DO_NOTHING, blank=True, null=True)
    appdate = models.DateField(blank=True, null=True)
    apptime = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APPOINTMENTS'


class Client(models.Model):
    client_id = models.AutoField(db_column='Client_id', primary_key=True)  # Field name made lowercase.
    fname = models.CharField(max_length=100, blank=True, null=True)
    lname = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(unique=True, max_length=100, blank=True, null=True)
    cl_password = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CLIENT'


class Company(models.Model):
    C_id = models.AutoField(primary_key=True, db_column='C_id')
    company_name = models.CharField(max_length=100, db_column='Company_Name', blank=True, null=True)
    company_address = models.CharField(max_length=255, db_column='Company_Address', blank=True, null=True)
    company_phone = models.CharField(max_length=15, db_column='Company_Phone', blank=True, null=True)
    company_email = models.CharField(max_length=100, db_column='Company_Email', blank=True, null=True)
    company_pw = models.CharField(max_length=255, db_column='Company_PW', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'COMPANY'


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True, db_column='Employee_id')
    fname = models.CharField(max_length=50, blank=True, null=True)
    lname = models.CharField(max_length=50, blank=True, null=True)
    c = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True)
    emp_password = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    is_admin = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')], default='N')

    class Meta:
        managed = False
        db_table = 'EMPLOYEE'



class Invoice(models.Model):
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

    class Meta:
        managed = False
        db_table = 'TASKPING'