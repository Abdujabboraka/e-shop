# Generated by Django 5.1.1 on 2024-10-20 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_announcement_deadline_alter_announcement_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
    ]