
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecentVisitPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_usable', models.BooleanField(default=True, verbose_name='사용여부')),
                ('creation_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='생성시간')),
                ('modify_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='수정시간')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('travel_Schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.TravelInformation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_usable', models.BooleanField(default=True, verbose_name='사용여부')),
                ('creation_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='생성시간')),
                ('modify_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='수정시간')),
                ('is_canceled', models.BooleanField(default=False, verbose_name='취소여부')),
                ('reversed_people', models.IntegerField(default=0, verbose_name='예약수')),
                ('concept', models.TextField(blank=True, verbose_name='여행컨셉')),
                ('age_generation', models.CharField(blank=True, max_length=50, verbose_name='연령대')),
                ('personal_request', models.TextField(blank=True, verbose_name='요청사항')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('travel_Schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.TravelSchedule')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_usable', models.BooleanField(default=True, verbose_name='사용여부')),
                ('creation_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='생성시간')),
                ('modify_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='수정시간')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('travel_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.TravelInformation')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
