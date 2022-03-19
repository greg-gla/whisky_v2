from django.db import models
from accounts.models import User

# Create your models here.
class Distillery(models.Model):
    NAME_MAX_LENGTH = 128
    LOCATION_MAX_LENGTH = 512
    DESCRIPTION_MAX_LENGTH = 1024

    name = models.CharField(max_length=NAME_MAX_LENGTH)
    logo = models.ImageField(max_length=100, blank=True, default='default.png')
    location = models.CharField(max_length=LOCATION_MAX_LENGTH)
    description = models.CharField(max_length=DESCRIPTION_MAX_LENGTH)
    
    class Meta:
        verbose_name_plural = 'Distilleries'


    def __str__(self) :
        return self.name

class Whisky(models.Model):
    NAME_MAX_LENGTH = 128
    DESCRIPTION_MAX_LENGTH = 512

    name = models.CharField(max_length=NAME_MAX_LENGTH)
    age = models.IntegerField(default=0)
    abv = models.IntegerField(default=0)
    description = models.CharField(max_length=DESCRIPTION_MAX_LENGTH)
    image = models.ImageField(max_length=100, blank=True, default='default.png')
    distillery = models.ForeignKey(Distillery,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Whiskies'

    def __str__(self):
        return self.name

class Rating(models.Model):
    VERBAL_RATING_MAX_LENGTH = 512

    numeric_rating = models.FloatField(default=0.0)
    verbal_rating = models.CharField(max_length=VERBAL_RATING_MAX_LENGTH)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    whisky_id = models.ForeignKey(Whisky,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) :
        return self.verbal_rating