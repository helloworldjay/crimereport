from django.db import models




class Congressperson(models.Model):
    name = models.CharField(max_length=50)
    district = models.CharField(max_length=1000)
    crimes = models.TextField()
    penalty = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    elected_num = models.IntegerField()
    party = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'congressperson'


class Saying(models.Model):
    speaker = models.CharField(max_length=50)
    saying = models.TextField()

    class Meta:
        managed = False
        db_table = 'saying'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'