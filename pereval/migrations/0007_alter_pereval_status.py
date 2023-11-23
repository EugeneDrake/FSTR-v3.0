
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pereval', '0006_alter_image_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pereval',
            name='status',
            field=models.CharField(choices=[('new', 'new'), ('pending', 'pending'), ('accepted', 'accepted'), ('rejected', 'rejected')], default='new', max_length=10),
        ),
    ]