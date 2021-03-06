# Generated by Django 3.0.9 on 2020-08-04 05:10

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields
import users.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='unique id')),
                ('pin', models.CharField(editable=False, max_length=25, unique=True, verbose_name='personal identity number')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('full_name', models.CharField(max_length=300, verbose_name='full name')),
                ('picture', models.ImageField(default='images/default/pic.png', upload_to=users.models.user_upload_to, verbose_name='picture')),
                ('phone_number', models.CharField(max_length=10, verbose_name='phone number')),
                ('date_of_birth', models.DateTimeField(null=True, verbose_name='date of birth')),
                ('born', django_countries.fields.CountryField(max_length=2, verbose_name='born')),
                ('nationality', django_countries.fields.CountryField(max_length=2, verbose_name='nationality')),
                ('expired_at', models.DateTimeField(default=users.models.get_expired_date, verbose_name='expired at')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Renew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Requested', 'Requested'), ('Accepted', 'Accepted'), ('Deny', 'Deny')], default='Requested', max_length=20, verbose_name='status')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='renews', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'renew',
                'verbose_name_plural': 'renews',
            },
        ),
        migrations.CreateModel(
            name='Fingerprint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to=users.models.fingerprint_upload_to, verbose_name='picture')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fingerprints', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'fingerprint',
                'verbose_name_plural': 'fingerprints',
            },
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='name')),
                ('description', models.TextField(verbose_name='description')),
                ('city', models.CharField(max_length=200, verbose_name='city')),
                ('sub_city', models.CharField(max_length=200, verbose_name='sub city')),
                ('type', models.CharField(choices=[('Sole Proprietorship', 'Sole Proprietorship'), ('Private Limited Company', 'Private Limited Company')], max_length=25, verbose_name='type')),
                ('status', models.CharField(choices=[('Requested', 'Requested'), ('Accepted', 'Accepted'), ('Deny', 'Deny')], default='Requested', max_length=20, verbose_name='status')),
                ('is_active', models.BooleanField(blank=True, null=True, verbose_name='is active')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('owners', models.ManyToManyField(blank=True, related_name='business_owners', to=settings.AUTH_USER_MODEL, verbose_name='owners')),
                ('requested_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='businesses', to=settings.AUTH_USER_MODEL, verbose_name='requested by')),
            ],
            options={
                'verbose_name': 'business',
                'verbose_name_plural': 'businesses',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', django_countries.fields.CountryField(max_length=2, verbose_name='country')),
                ('city', models.CharField(max_length=100, verbose_name='city')),
                ('street', models.CharField(max_length=100, verbose_name='street')),
                ('house_number', models.CharField(max_length=100, verbose_name='house number')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'address',
                'verbose_name_plural': 'addresses',
            },
        ),
    ]
