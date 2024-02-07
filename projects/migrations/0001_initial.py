from django.db import models, migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('github', models.URLField()),
                ('linkedin', models.URLField()),
                ('bio', models.TextField()),
            ],
        ),
    ]
