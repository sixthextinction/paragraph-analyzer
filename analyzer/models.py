from django.db import models
from django.contrib.postgres.fields import HStoreField

# Create your models here.
from django.urls import reverse
from django.utils.text import slugify


class Post(models.Model):
    title = models.TextField(max_length=120)
    input = models.TextField()
    analysis = HStoreField()  # format = "word" : count
    analyzed_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    slug = models.SlugField(unique=True)

    # overridden save method to add the slug
    def save(self, *args, **kwargs):
        # account for python's lookup stupidity for input containing 'items'
        self.input= self.input.replace('items', 'items_')

        # generate the title
        self.title = self.input[:20] + "..."

        # make word list
        word_list = self.input.lower().split()

        # put/update results into instance.analysis dict
        analysis = {}
        for word in word_list:
            if word in analysis:
                analysis[word] += 1
            else:
                analysis[word] = 1

        self.analysis = analysis #wait what, it supports string:int pairs?!
        # now do the rest
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.input[:20] + "-" + str(self.id))  # truncate to first 20 chars and slugify that
            # self.save()
            super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})
