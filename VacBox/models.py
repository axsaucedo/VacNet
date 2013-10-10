from django.db import models
from accounts.models import InstitutionProfile
import datetime
from django.utils.timezone import utc

class VaccineCase(models.Model):
    caseid = models.AutoField(primary_key=True)
    datecreated = models.DateTimeField("Date created", default=datetime.datetime.utcnow().replace(tzinfo=utc))
    vaccines = models.IntegerField("Total vaccines", default=0)
    country = models.CharField("City delivery", max_length=100)
    password = models.CharField("Password", max_length=100)

    def __unicode__(self):
        return self.vaccines + ' in ' + self.country;


class VaccineRecord(models.Model):
    vaccinerecordid = models.AutoField(primary_key=True)


class Person(models.Model):
    GENDER_CHOICES = (
            ('M', 'Male'),
            ('F', 'Female'),
        )

    personid = models.AutoField(primary_key=True)
    datecreated = models.DateTimeField("Date created", default=datetime.datetime.utcnow().replace(tzinfo=utc))
    firstname = models.CharField("First name", max_length=100)
    lastname = models.CharField("Last name", max_length=100)
    dob = models.DateField('Date of Birth');
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M', null=True)
    mobile = models.CharField("Phone Number", max_length=20)
    guardian = models.CharField("Parent or guardian", max_length=100)
    guardianmobile = models.CharField("Parent or guardian phone number", max_length=100)
    vaccinerecord = models.OneToOneField(VaccineRecord, verbose_name="Vaccine Record Reference")


class VaccineApplied(models.Model):
    vaccineappliedid = models.AutoField(primary_key=True)
    vaccinetype = models.CharField("Vaccine type", max_length=100)
    case = models.ForeignKey(VaccineRecord, verbose_name="Vaccine Record Reference")
    person = models.OneToOneField(Person, verbose_name="Person Reference")

