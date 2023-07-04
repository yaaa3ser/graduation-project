from django.db import models

class Experiment(models.Model):
    name = models.CharField(max_length=1000)
    observation = models.CharField(max_length=1000)
    conclusion = models.CharField(max_length=1000)
    
    def __str__(self) -> str:
        return self.name

class Equipment(models.Model):
    EQUIPMENT_CHOICES = (
        ('Beaker', 'Beaker'),
        ('Bunsen Burner', 'Bunsen Burner'),
        ('Sunflower Paper', 'Sunflower Paper'),
        ('Pipette', 'Pipette'),
        ('Test Tube', 'Test Tube'),
        ('Lighter', 'Lighter'),
        ('Test Tube', 'Test Tube')
        # add more choices here
        
    )
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE,related_name='equipments')
    name = models.CharField(max_length=1000, choices=EQUIPMENT_CHOICES)
    
    def __str__(self) -> str:
        return self.name

class Chemicals(models.Model):
    CHEMICALS_CHOICES = (
        ('Water', 'Water'),
        ('Starch', 'Starch'),
        ('Sodium Hydroxide', 'Sodium Hydroxide'),
        # add more choices here
        
    )
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE,related_name='chemicals')
    name = models.CharField(max_length=1000, choices=CHEMICALS_CHOICES)
    symbol = models.CharField(max_length=1000)
    
    def __str__(self) -> str:
        return self.name

class Steps(models.Model):
    VERBS = (
        ('Boil', 'Boil'),
        ('Add', 'Add'),
        ('Light', 'Light'),
        # add more choices here
    )

    EQUIPMENT = (
        ('Beaker', 'Beaker'),
        ('Bunsen Burner', 'Bunsen Burner'),
        ('Sunflower Paper', 'Sunflower Paper'),
        ('Pipette', 'Pipette'),
        ('Test Tube', 'Test Tube'),
        ('Lighter', 'Lighter'),
        ('Test Tube', 'Test Tube')
        # add more choices here
    )
    
    CHEMICALS = (
        ('Water', 'Water'),
        ('Starch', 'Starch'),
        ('Sodium Hydroxide', 'Sodium Hydroxide'),
        # add more choices here
    )

    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE, related_name='steps')
    verb = models.CharField(max_length=100, choices=VERBS)
    quantity = models.IntegerField(blank=True, null=True)
    chemical = models.CharField(max_length=100, choices=CHEMICALS, blank=True, null=True)
    equipment = models.CharField(max_length=100, choices=EQUIPMENT, blank=True, null=True)

    def __str__(self) -> str:
        if not self.quantity:
            self.quantity = ''
        if not self.chemical:
            self.chemical = ''
        if not self.equipment:
            self.equipment = ''
        return f'{self.verb} {self.quantity} {self.chemical} {self.equipment}'
    
    @property
    def formatted_step(self) -> str:
        if not self.quantity:
            self.quantity = ''
        else:
            self.quantity = f'{self.quantity} ml'
        if not self.chemical:
            self.chemical = ''
        if not self.equipment:
            self.equipment = ''
        if self.equipment and self.chemical:
            self.equipment = f'to {self.equipment}'
            self.chemical = f'from {self.chemical}'
        return f'{self.verb} {self.quantity} {self.chemical} {self.equipment}'
