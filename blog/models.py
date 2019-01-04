from django.db import models

# create a blog model
#-title
#-public_date
#-body
#-image

class Blog(models.Model):
    title = models.CharField(max_length=100) #maximum length for CharField is 255
    pub_date = models.DateTimeField()
    body = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='imgs/')

#add the blog app to the settings

#create a migration

#migrate

#add to the admin
