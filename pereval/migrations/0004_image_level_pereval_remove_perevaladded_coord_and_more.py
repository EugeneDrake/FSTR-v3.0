# Generated by Django 4.2.7 on 2023-11-05 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pereval', '0003_perevaladded_coord_perevalimages_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
                ('data', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winter', models.TextField(blank=True, null=True)),
                ('summer', models.TextField(blank=True, null=True)),
                ('autumn', models.TextField(blank=True, null=True)),
                ('spring', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pereval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='new', max_length=10)),
                ('beauty_title', models.TextField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('other_titles', models.TextField(blank=True, null=True)),
                ('connect', models.TextField(blank=True, null=True)),
                ('add_time', models.TimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='perevaladded',
            name='coord',
        ),
        migrations.DeleteModel(
            name='PerevalAreas',
        ),
        migrations.RemoveField(
            model_name='perevalimages',
            name='image',
        ),
        migrations.RemoveField(
            model_name='perevalimages',
            name='pereval',
        ),
        migrations.DeleteModel(
            name='SprActivitiesTypes',
        ),
        migrations.AlterModelTable(
            name='coords',
            table=None,
        ),
        migrations.AlterModelTable(
            name='user',
            table=None,
        ),
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
        migrations.DeleteModel(
            name='Images',
        ),
        migrations.DeleteModel(
            name='PerevalAdded',
        ),
        migrations.DeleteModel(
            name='PerevalImages',
        ),
        migrations.AddField(
            model_name='pereval',
            name='coords',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pereval.coords'),
        ),
        migrations.AddField(
            model_name='pereval',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pereval.level'),
        ),
        migrations.AddField(
            model_name='pereval',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pereval.user'),
        ),
        migrations.AddField(
            model_name='image',
            name='pereval',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='pereval.pereval'),
        ),
    ]