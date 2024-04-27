from django.db import models


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    class Meta:
        db_table = 'comment'

    def __str__(self):
        return f"{self.author} on '{self.post}'"

