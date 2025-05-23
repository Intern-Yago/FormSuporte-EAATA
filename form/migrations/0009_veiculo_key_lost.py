# Generated by Django 5.2.1 on 2025-05-13 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0008_delete_newveiculo_remove_veiculo_immo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='key_lost',
            field=models.CharField(blank=True, choices=[('', '---------'), ('allOBD', 'All support OBD method'), ('partOBD', 'Part of the models support OBD method'), ('allBENCH', 'All support on-bench/boot method'), ('partBENCH', 'Part of the models support on-bench/boot method'), ('notreq', 'Not required'), ('none', 'Not supported')], max_length=10, verbose_name='Key lost'),
        ),
    ]
