from django.db import models

# Create your models here.


class RegForm(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    dob = models.DateField()
    gender = models.CharField(max_length=60)
    address = models.CharField(max_length=60)
    mobile = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    aadhar = models.IntegerField()
    fname = models.CharField(max_length=60)
    foccupation = models.CharField(max_length=60)
    institutename = models.CharField(max_length=100)
    course = models.CharField(max_length=60)
    presentyear = models.CharField(max_length=60)
    percentage12 = models.CharField(max_length=60)
    cgpa = models.CharField(max_length=60)
    photograph = models.ImageField(upload_to='Photographs', default="")
    marksheet12 = models.FileField(upload_to='Marksheets_12', default="")
    lmarksheet = models.FileField(upload_to='Latest_Marksheets', default="")
    bletter = models.FileField(upload_to='Bonafied_Letters', default="")
    Designation = models.CharField(max_length=60, default=None)
    CPF = models.CharField(max_length=60, default=None)
    Section = models.CharField(max_length=60, default=None)
    Location = models.CharField(max_length=60, default=None)
    PhoneNumber = models.CharField(max_length=15, default=None)
    MobileNumber = models.CharField(max_length=15, default=None)
    counter = models.IntegerField(default=0)

    def __str__(self):
        return "%s (%s)" % (self.aadhar, self.name)
