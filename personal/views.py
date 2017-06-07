from django.shortcuts import render
from django.views import generic
from .models import  Story
from django.templatetags.static import static
import os
import mysite
import re

def index(request):
    return render(request, 'personal/home.html')

class detailView(generic.DetailView):
    model = Story
    template_name = 'personal/storydetail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        story_file = context.get("story").storyfile
        story_obj  = context.get("story")
        story_obj.read_count = story_obj.read_count+1
        story_obj.save()
        lines = ""
        content = "<p>"
        with open(mysite.settings.BASE_DIR+'/Stories/'+story_file, 'r') as content_file:
            #content = content_file.read()
            for line in content_file:
                if re.match(r'^\s*$', line):
                    line="</p><p>"
                content = content+line
        context['story_text'] = content
        return self.render_to_response(context)