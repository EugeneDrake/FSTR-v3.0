from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pereval', '0003_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(blank=True, max_length=320, null=True),
        ),
    ]