from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]
    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('github_url', models.URLField()),
                ('keyword', models.CharField(max_length=50)),
                ('key_skill', models.CharField(max_length=50)),
                ('profile', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='projects.Profile')),
            ],
        ),
    ]
