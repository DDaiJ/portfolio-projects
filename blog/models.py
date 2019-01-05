from django.db import models

# create a blog model
#-title
#-public_date
#-body
#-image

class Blog(models.Model):
    title = models.CharField(max_length=100) #maximum length for CharField is 255
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='imgs/')

    def pub_date_pretty(self):
        return self.pub_date.strftime('%c')

    def __str__(self): #set the blog id in admin same as the title
        return self.title

#add the blog app to the settings

#create a migration

#migrate

#add to the admin
