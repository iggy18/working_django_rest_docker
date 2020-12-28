from django.db import models
from django.contrib.auth import get_user_model

class Post(models.Model):
    #title box narrow text box
    title = models.CharField(max_length= 255)
    #text field large text box for body
    body = models.TextField(default="")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        """
        returns short self description
        """
        return self.title, self.author
    