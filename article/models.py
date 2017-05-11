from __future__ import unicode_literals

from django.db import models

from django.core.urlresolvers import reverse
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100)
    category = models.CharField(max_length = 50, blank = True)
    date_time = models.DateTimeField(auto_now_add = True)
    content = models.TextField(blank = True, null = True)
    views = models.PositiveIntegerField(default = 0) 
    
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])
    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id': self.id})
        return "syx666.com:8080%s" % path

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['date_time']

