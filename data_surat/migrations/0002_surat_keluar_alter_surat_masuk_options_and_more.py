# Generated by Django 4.0.6 on 2022-10-08 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_surat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='surat_keluar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_surat', models.CharField(max_length=100)),
                ('tanggal_terima', models.DateField()),
                ('nomor_surat', models.IntegerField()),
                ('pengirim', models.CharField(max_length=100)),
                ('perihal', models.CharField(max_length=100)),
                ('ditunjukan', models.CharField(max_length=100)),
                ('file', models.FileField(help_text='Upload document', upload_to='surat_keluar/%Y/%m/%d')),
            ],
            options={
                'verbose_name_plural': 'Surat Keluar',
            },
        ),
        migrations.AlterModelOptions(
            name='surat_masuk',
            options={'verbose_name_plural': 'Surat Masuk'},
        ),
        migrations.AlterField(
            model_name='surat_masuk',
            name='file',
            field=models.FileField(help_text='Upload document', upload_to='surat_masuk/%Y/%m/%d'),
        ),
    ]
