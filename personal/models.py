from django.db import models

# Create your models here.


class Story(models.Model):
    story_title = models.CharField(max_length=200) #Story title
    published = models.DateTimeField('date published') #Story published on storyhut
    writer = models.CharField(max_length=200) #WriterName
    collection=models.CharField(max_length=200) #Collection/Book name
    cover_loc=models.CharField(max_length=400) #Cover Art location
    brief= models.CharField(max_length=250)
    likes=models.IntegerField() #Totallikes
    dislikes=models.IntegerField() #Total dislikes
    read_count=models.IntegerField() #Story read time
    storyfile = models.CharField(max_length=250)

    def display_text_file(self):

    # with open(self.text.path) as fp:
    #     return fp.read().replace('\n', '<br>')
        print("Ha ha haa")
        return "sample text"

