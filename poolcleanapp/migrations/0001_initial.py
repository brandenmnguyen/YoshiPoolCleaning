# Generated by Django 4.2.7 on 2024-04-16 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoice_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('payment_method', models.CharField(blank=True, max_length=50, null=True)),
                ('card_name', models.CharField(blank=True, max_length=100, null=True)),
                ('expdate', models.DateField(blank=True, db_column='ExpDate', null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('card_number', models.CharField(blank=True, max_length=16, null=True)),
                ('cvv_code', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'INVOICE',
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
                ('cl_password', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'CLIENT',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('c_id', models.AutoField(db_column='C_id', primary_key=True, serialize=False)),
                ('company_name', models.CharField(blank=True, db_column='Company_Name', max_length=100, null=True)),
                ('company_address', models.CharField(blank=True, db_column='Company_Address', max_length=255, null=True)),
                ('company_phone', models.CharField(blank=True, db_column='Company_Phone', max_length=15, null=True)),
                ('company_email', models.CharField(blank=True, db_column='Company_Email', max_length=100, null=True)),
                ('company_pw', models.CharField(blank=True, db_column='Company_PW', max_length=255, null=True)),
            ],
            options={
                'db_table': 'COMPANY',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Taskping',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('n', 'In progress'), ('y', 'Completed')], default='n', max_length=1)),
                ('taskname', models.CharField(choices=[('---', '---'), ('Inspect the Pool.', 'Inspect the Pool.'), ('Clean the Pump Basket', 'Clean the Pump Basket'), ('Scrub Pool Walls.', 'Scrub Pool Walls.'), ('Skim the Pool', 'Skim the Pool'), ('Empty the Skimmer Basket.', 'Empty the Skimmer Basket.'), ('Vacuum the Pool', 'Vacuum the Pool'), ('Backwash Sand and DE Filters', 'Backwash Sand and DE Filters'), ('Test the Pool Water and Add Chemicals', 'Test the Pool Water and Add Chemicals')], default='---', max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('c_id', models.ForeignKey(blank=True, db_column='C_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='poolcleanapp.company')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='poolcleanapp.client')),
            ],
            options={
                'db_table': 'TASKPING',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProviderAvailableTimes',
            fields=[
                ('appointment_id', models.AutoField(primary_key=True, serialize=False)),
                ('appdate', models.DateField(blank=True, null=True)),
                ('apptime', models.TimeField(blank=True, null=True)),
                ('c', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='poolcleanapp.company')),
            ],
            options={
                'db_table': 'PROVIDERAVAILABLETIMES',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(db_column='Employee_id', primary_key=True, serialize=False)),
                ('fname', models.CharField(blank=True, max_length=50, null=True)),
                ('lname', models.CharField(blank=True, max_length=50, null=True)),
                ('emp_password', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('is_admin', models.CharField(blank=True, max_length=1, null=True)),
                ('c', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='poolcleanapp.company')),
            ],
            options={
                'db_table': 'EMPLOYEE',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('appointment_id', models.AutoField(primary_key=True, serialize=False)),
                ('appdate', models.DateField(blank=True, null=True)),
                ('apptime', models.TimeField(blank=True, null=True)),
                ('c', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='poolcleanapp.company')),
                ('cl', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='poolcleanapp.client')),
            ],
            options={
                'db_table': 'appointments',
                'managed': True,
            },
        ),
    ]
