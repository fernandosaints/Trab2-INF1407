from django.db import models
class Player(models.Model):
  id = models.AutoField(primary_key=True),
  name = models.CharField(
  max_length=100, help_text="Enter player's name")
  team = models.CharField(
  max_length=100, help_text="Enter player's team")
  nation = models.CharField(
  max_length=100, help_text="Enter player's nation")
  creator = models.CharField(
        verbose_name='Creator', max_length=30, editable=False)
  def __str__(self):
    return self.name

# Create your models here.
