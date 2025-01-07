from django.db import models

# Home section

class Home(models.Model):
    name = models.CharField(max_length=30)
    greeting_1 = models.CharField(max_length=30)
    greeting_2 = models.CharField(max_length=30)
    picture = models.ImageField(upload_to='picture/')
    updated = models.DateTimeField(auto_now=True)
    fav = models.ImageField(upload_to='icons/', default='../static/img/favicon.png')
    
    def __str__(self):
        return self.name
    
# About section

class About(models.Model):
    heading = models.CharField(max_length=100) 
    career = models.CharField(max_length=50) 
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='profile/')   
    updated = models.DateTimeField(auto_now=True)
    numb = models.CharField(max_length=20,default='+91 000-000-0000')
    addr = models.CharField(max_length=200,default='Bhagalpur, Bihar, India')
    email = models.CharField(max_length=50,default='snk.22104@gmail.com')
    resl = models.URLField(max_length=200,default='https://drive.google.com/file/d/1zcba3G7v706wHnIUsJtunsIUPb8arb-_/view')
    
    def __str__(self):
        return self.career
    
class Profile(models.Model):
    about = models.ForeignKey(About,on_delete=models.CASCADE)
    social_name = models.CharField(max_length=10)
    link = models.URLField(max_length=200)
    
#Skills section

class Category(models.Model):
    name = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'skill'
        verbose_name_plural = 'skills'
        
    def __str__(self):
        return self.name
    
class Skills(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    skills_name = models.CharField(max_length=50)
    
# Portfolio section

class Portfolio(models.Model):
    image =   models.ImageField(upload_to='portfolio/') 
    link = models.URLField(max_length=200)
    name = models.CharField(max_length=50,default='name')
      
    def __str__(self):
        return self.name
        
        
class Certification(models.Model):
    image =   models.ImageField(upload_to='portfolio/') 
    
    name = models.CharField(max_length=50,default='name')
    org = models.CharField(max_length=50,default='org')
      
    def __str__(self):
        return self.name              
        