# Generated by Django 4.0.3 on 2022-06-29 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0009_grade_alter_answer_created_at_profile_grade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='grade',
        ),
        migrations.AddField(
            model_name='profile',
            name='year_in_school',
            field=models.CharField(choices=[('1학년', '1학년'), ('2학년', '2학년'), ('3학년', '3학년'), ('4학년', '4학년'), ('대학원생', '대학원생'), ('졸업생', '졸업생')], default='1학년', max_length=10),
        ),
        migrations.DeleteModel(
            name='Grade',
        ),
    ]
