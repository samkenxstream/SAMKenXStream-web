# Generated by Django 2.2.3 on 2019-09-28 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kudos', '0006_token_override_display_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='bulktransfercoupon',
            name='tag',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]