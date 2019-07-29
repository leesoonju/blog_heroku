from django.db import models

class Blog(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    objects = models.Manager()

    def __str__(self):
        return self.title


    def summary(self):
        return self.body[:100]


