# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Appointments(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    cl = models.ForeignKey('Client', models.DO_NOTHING, blank=True, null=True)
    c = models.ForeignKey('Company', models.DO_NOTHING, blank=True, null=True)
    appdate = models.DateField(blank=True, null=True)
    apptime = models.TimeField(blank=True, null=True)

    def get_client(self):
        return self.cl  # Corrected to return the actual ForeignKey field to Client

    def get_company(self):
        return self.c  # Corrected to return the actual ForeignKey field to Company

    class Meta:
        managed = True
        db_table = 'appointments'



class ProviderAvailableTimes(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    c = models.ForeignKey('Company', models.DO_NOTHING, to_field='c_id', blank=True, null=True)
    appdate = models.DateField(blank=True, null=True)
    apptime = models.TimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'PROVIDERAVAILABLETIMES'

        

class Client(models.Model):
    client_id = models.AutoField(db_column='Client_id', primary_key=True)  # Field name made lowercase.
    fname = models.CharField(max_length=100, blank=True, null=True)
    lname = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(unique=True, max_length=100, blank=True, null=True)
    cl_password = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'CLIENT'


class Company(models.Model):
    c_id = models.AutoField(db_column='C_id', primary_key=True)  # Field name made lowercase.
    company_name = models.CharField(db_column='Company_Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    company_address = models.CharField(db_column='Company_Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    company_phone = models.CharField(db_column='Company_Phone', max_length=15, blank=True, null=True)  # Field name made lowercase.
    company_email = models.CharField(db_column='Company_Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
    company_pw = models.CharField(db_column='Company_PW', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'COMPANY'


class Employee(models.Model):
    employee_id = models.AutoField(db_column='Employee_id', primary_key=True)  # Field name made lowercase.
    fname = models.CharField(max_length=50, blank=True, null=True)
    lname = models.CharField(max_length=50, blank=True, null=True)
    c = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True)
    emp_password = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_admin = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'EMPLOYEE'


class Invoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, models.DO_NOTHING, blank=True, null=True)
    c = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payment_method = models.CharField(max_length=50, blank=True, null=True)
    card_name = models.CharField(max_length=100, blank=True, null=True)
    expdate = models.DateField(db_column='ExpDate', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=100, blank=True, null=True)
    card_number = models.CharField(max_length=16, blank=True, null=True)
    cvv_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'INVOICE'


class Taskping(models.Model):
    TASK_TASKNAME_CHOICES = [
        ('---','---'),
        ('Inspect the Pool.', 'Inspect the Pool.'),
        ('Clean the Pump Basket', 'Clean the Pump Basket'),
        ('Scrub Pool Walls.', 'Scrub Pool Walls.'),
        ('Skim the Pool', 'Skim the Pool'),
        ('Empty the Skimmer Basket.', 'Empty the Skimmer Basket.'),
        ('Vacuum the Pool', 'Vacuum the Pool'),
        ('Backwash Sand and DE Filters', 'Backwash Sand and DE Filters'),
        ('Test the Pool Water and Add Chemicals', 'Test the Pool Water and Add Chemicals')
    ]
    TASK_STATUS_CHOICES = [
        ('n', 'In progress'),
        ('y', 'Completed'),
    ]

    task_id = models.AutoField(primary_key=True)
    status = models.CharField(
        max_length=1,
        choices=TASK_STATUS_CHOICES,
        default='n'
    )
    taskname = models.CharField(
        max_length=100,
        choices=TASK_TASKNAME_CHOICES,
        default='---'
    )
    description = models.TextField(blank=True, null=True)
    client = models.ForeignKey('Client', on_delete=models.CASCADE, blank=True, null=True) 
    c_id = models.ForeignKey('Company', on_delete=models.CASCADE, db_column='C_id', blank=True, null=True)  
    updated_at = models.DateTimeField(auto_now=True)

    def get_client(self):
        return self.client

    def get_company(self):
        return self.c_id

    class Meta:
        managed = True
        db_table = 'TASKPING'

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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
        db_table = 'client'


class Company(models.Model):
    c_id = models.AutoField(db_column='C_id', primary_key=True)  # Field name made lowercase.
    company_name = models.CharField(db_column='Company_Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    company_address = models.CharField(db_column='Company_Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    company_phone = models.CharField(db_column='Company_Phone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    company_email = models.CharField(db_column='Company_Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
    company_pw = models.CharField(db_column='Company_PW', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'company'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

class ProviderAvailableTimes(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    c = models.ForeignKey('Company', models.DO_NOTHING, to_field='c_id', blank=True, null=True)
    appdate = models.DateField(blank=True, null=True)
    apptime = models.TimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'PROVIDERAVAILABLETIMES'

