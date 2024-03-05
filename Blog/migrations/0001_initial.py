# Generated by Django 4.2.3 on 2024-01-10 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('subheading', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('content1', models.TextField()),
                ('image', models.ImageField(upload_to='media/pics')),
                ('imagedetail', models.CharField(max_length=120)),
                ('content2', models.TextField()),
                ('placeholder', models.URLField()),
                ('category', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('comment', models.CharField(max_length=255)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.blogdetail')),
            ],
        ),
    ]