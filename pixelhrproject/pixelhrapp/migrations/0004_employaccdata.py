# Generated by Django 4.2.2 on 2024-04-06 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixelhrapp', '0003_reimbusement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employaccdata',
            fields=[
                ('eacc_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(default='', max_length=255)),
                ('fullname', models.CharField(default='', max_length=255)),
                ('password', models.CharField(default='', max_length=255)),
                ('email', models.CharField(default='', max_length=255)),
                ('phoneno', models.CharField(default='', max_length=255)),
                ('address', models.CharField(default='', max_length=500)),
                ('gender', models.CharField(default='', max_length=500)),
                ('dateofbirth', models.CharField(default='', max_length=50)),
                ('MaritalStatus', models.CharField(default='', max_length=50)),
                ('EmployeePhotoPath', models.CharField(default='', max_length=1000)),
                ('role', models.CharField(default='', max_length=255)),
                ('department', models.CharField(default='', max_length=255)),
                ('jobtitle', models.CharField(default='', max_length=255)),
                ('manager', models.CharField(default='', max_length=255)),
                ('dateofjoin', models.CharField(default='', max_length=255)),
                ('EmpStatus', models.CharField(default='', max_length=255)),
                ('EmpType', models.CharField(default='', max_length=255)),
                ('WorkLoc', models.CharField(default='', max_length=1000)),
                ('SickLeavecount', models.CharField(default='', max_length=255)),
                ('PrivilegeLeavecount', models.CharField(default='', max_length=255)),
                ('CasualLeavecount', models.CharField(default='', max_length=255)),
                ('MaternityLeavecount', models.CharField(default='', max_length=255)),
            ],
        ),
    ]