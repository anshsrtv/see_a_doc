from django.db import models

class Patient(models.Model):
    """
    User type: Pateient
    """
    name=models.CharField(max_length=500)
    contact=models.CharField(max_length=10)
    email=models.EmailField()
    DOB= models.DateField()
    gender = models.CharField(max_length=1, choices=[['M','Male'],['F','Female']])
    symptoms=models.TextField()
    weight = models.IntegerField()

    def __str__(self):
        return str(self.pk)+'-'+self.name+'-'+self.gender

class Hospital(models.Model):
    """
    Model to store hospital data.
    """
    name=models.CharField(max_length=500)
    location=models.TextField()
    about = models.CharField(max_length=500)
    details= models.TextField()
    rating = models.DecimalField(decimal_places=2, max_digits=3)
    email = models.EmailField()
    website = models.URLField()
    
    def __str__(self):
        return str(self.pk)+'-'+self.name

class Doctor(models.Model):
    """
    User type: Doctor
    """
    
    name=models.CharField(max_length=500)
    contact=models.CharField(max_length=10)
    email=models.EmailField()
    DOB= models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=[['M','Male'],['F','Female']])
    specialization = models.CharField(max_length=300)
    qualification = models.CharField(max_length=300)
    language = models.CharField(max_length=300)
    experience = models.IntegerField()
    about= models.CharField(max_length=500, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='media/profile_pic', null=True, blank=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    rating = models.DecimalField(decimal_places=2, max_digits=3)
    normal_charges = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return str(self.pk)+'-'+self.name+'-'+self.gender+'-'+self.specialization


