from django.db import models

# Create your models here.
class Food(models.Model):
    food_Id = models.BigAutoField(primary_key=True)
    food_Name = models.CharField(max_length=30)
    food_Type = models.CharField(max_length=30)
    food_Price = models.FloatField()
    food_Description = models.TextField()
    food_Image = models.ImageField(upload_to='foodimg/',default='NO_Image')

    def __str__(self) -> str:
        return self.food_Name