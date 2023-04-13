from django.db import models

class Experiment(models.Model):
    name = models.CharField(max_length=1000)
    observation = models.CharField(max_length=1000)
    conclusion = models.CharField(max_length=1000)

class Equipment(models.Model):
    EQUIPMENT_CHOICES = (
        ('دورق', 'دورق'),
        ('موقد', 'موقد'),
        ('ورقة عباد شمس', 'ورقة عباد شمس'),
        ('سحاحة', 'سحاحة'),
        ('ماصة', 'ماصة'),
        ('ولاعة', 'ولاعة'),
        ('انبوبة اختبار', 'انبوبة اختبار'),
        
    )
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE,related_name='equipments')
    name = models.CharField(max_length=1000, choices=EQUIPMENT_CHOICES)

class Chemicals(models.Model):
    CHEMICALS_CHOICES = (
        ('ماء', 'ماء'),
        ('محلول نشا', 'محلول نشا'),
        ('محلول لوغول', 'محلول لوغول'),
        
    )
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE,related_name='chemicals')
    name = models.CharField(max_length=1000, choices=CHEMICALS_CHOICES)
    symbol = models.CharField(max_length=1000)

class Steps(models.Model):
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE, related_name='steps')
    step = models.CharField(max_length=1000)
    
    def __str__(self) -> str:
        return self.step