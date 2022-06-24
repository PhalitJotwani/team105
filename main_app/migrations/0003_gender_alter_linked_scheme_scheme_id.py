# Generated by Django 4.0.5 on 2022-06-24 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_volunteer_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='linked_scheme',
            name='scheme_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.scheme'),
        ),
    ]
