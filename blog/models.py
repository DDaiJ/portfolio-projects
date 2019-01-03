from django.db import models

# create a blog model
#-title
#-public_date
#-body
#-image

class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateField(auto_now=True)
    body = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='imgs/', height_field=200)

#add the blog app to the settings

#create a migration

#migrate

#add to the admin
