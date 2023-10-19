from django.db import models

# Create your models here.
class WorkShop(models.Model):
    comment = models.CharField(max_length=30)
    pub_date = models.DateTimeField()
    likes = models.PositiveIntegerField(default=0)
    emoji_CHOICES = (
        ('happy', '😊'), 
        ('congrats', '🥳'), 
        ('wink', '😆'), 
        ('pien', '🥺'), 
        ('hi', '👋'), 
        ('heart', '💗'), 
        ('lion', '🦁'),
    )
    emoji = models.CharField(max_length=20, choices=emoji_CHOICES, default='happy')
    # image = models.ImageField(blank=True)
    
    def __str__(self):
        return self.comment

