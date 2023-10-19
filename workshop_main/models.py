from django.db import models

# Create your models here.
class WorkShop(models.Model):
    comment = models.CharField(max_length=30)
    pub_date = models.DateTimeField()
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    sadness = models.IntegerField(default=0)
    image = models.ImageField(blank=True)
    
    def __str__(self):
        return self.comment
    


