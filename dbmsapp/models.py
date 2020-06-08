from django.db import models

# Create your models here.

class tea(models.Model):
    team_id=models.IntegerField(' team_id',default=1)
    team_name=models.CharField('team_name',max_length=29,default=1)
    # class Meta:
    #     # Gives the proper plural name for admin
    #     verbose_name_plural = "Categories"

    
    def  __str__(self):
        # danger: might expose the password
        return '{}'.format( self.team_name)

class playe(models.Model):
    
    # team_name = models.ForeignKey( tea, on_delete=models.CASCADE)
    team_name=models.CharField('team_name',default=1,max_length=256)
    player_id=models.IntegerField(' player_id',default=1)
    player_name=models.CharField('player_name',max_length=29,default=1)
    no_of_matches=models.IntegerField('no_of_matches',default=1)
    total_score=models.IntegerField('Total Score',default=1)
    total_wicket=models.IntegerField('Total wicket',default=1)
    def __str__(self):
        return  '{}/{}/{}/{}'.format(self.player_id,self.player_name,self.no_of_matches,self.total_score,self.total_wicket)
class Employee(models.Model):  
        eid = models.CharField(max_length=20)  
        ename = models.CharField(max_length=100)  
        eemail = models.EmailField()  
        econtact = models.CharField(max_length=15)  

class player(models.Model):
    
    # team_name = models.ForeignKey( tea, on_delete=models.CASCADE)
    team_name=models.CharField('team_name',default=1,max_length=256)
    player_id=models.IntegerField(' player_id',default=1)
    player_name=models.CharField('player_name',max_length=29,default=1)
    no_of_matches=models.IntegerField('no_of_matches',default=1)
    total_score=models.IntegerField('Total Score',default=1)
    total_wicket=models.IntegerField('Total wicket',default=1)
    def __str__(self):
        return  '{}/{}/{}/{}'.format(self.player_id,self.player_name,self.no_of_matches,self.total_score,self.total_wicket)  
        
              
         


     

        

    
    
