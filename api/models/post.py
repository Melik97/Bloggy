from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    category = models.ForeignKey("Category", null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        db_table = 'post'
        # indexes = [models.Index(fields='title', name='name_idx'),]

    def __str__(self):
        return self.title

