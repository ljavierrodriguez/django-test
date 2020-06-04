from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    body = models.TextField()
    #author = models.CharField(max_length=100, null=False, blank=False, default="Anonimous")
    author = models.ForeignKey('auth.User', null=False, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return "%s" % self.title


class Commment(models.Model):
    comment = models.TextField(blank=False, null=False)
    date_comment = models.DateTimeField(auto_now=True)
    blog = models.ForeignKey('Blog', null=False, on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', null=False, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return "%s" % self.comment

