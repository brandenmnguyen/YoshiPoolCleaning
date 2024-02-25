# Generated by Django 5.0.2 on 2024-02-25 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('appointment_id', models.AutoField(primary_key=True, serialize=False)),
                ('appdate', models.DateField(blank=True, null=True)),
                ('apptime', models.TimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'APPOINTMENTS',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.AutoField(db_column='Client_id', primary_key=True, serialize=False)),
                ('fname', models.CharField(blank=True, max_length=100, null=True)),
                ('lname', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('cl_password', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'CLIENT',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('c_id', models.AutoField(db_column='C_id', primary_key=True, serialize=False)),
                ('company_name', models.CharField(blank=True, db_column='Company_Name', max_length=100, null=True)),
                ('company_address', models.CharField(blank=True, db_column='Company_Address', max_length=255, null=True)),
                ('company_phone', models.CharField(blank=True, db_column='Company_Phone', max_length=20, null=True)),
                ('company_email', models.CharField(blank=True, db_column='Company_Email', max_length=100, null=True)),
                ('company_pw', models.CharField(blank=True, db_column='Company_PW', max_length=20, null=True)),
            ],
            options={
                'db_table': 'COMPANY',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(db_column='Employee_id', primary_key=True, serialize=False)),
                ('fname', models.CharField(blank=True, max_length=50, null=True)),
                ('lname', models.CharField(blank=True, max_length=50, null=True)),
                ('emp_password', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'EMPLOYEE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('payment_date', models.DateField(blank=True, null=True)),
                ('received_date', models.DateField(blank=True, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('payment_method', models.CharField(blank=True, max_length=50, null=True)),
                ('card_name', models.CharField(blank=True, max_length=100, null=True)),
                ('expdate', models.DateField(blank=True, db_column='ExpDate', null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('reference_number', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'PAYMENT',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Taskping',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(blank=True, max_length=1, null=True)),
                ('taskname', models.CharField(blank=True, db_column='taskName', max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'TASKPING',
                'managed': False,
            },
        ),
    ]
