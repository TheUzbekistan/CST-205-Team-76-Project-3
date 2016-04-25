from __future__ import unicode_literals

from django.db import models

 
class ChatRoom(models.Model):
    name = models.CharField(max_length=200)
 
    def __unicode__(self):
    	return self.name
'''
We're building a model for storing a ChatRoom. Note that this specific tutorial doesn't go so far as to store actual chat messages to disk, so we won't need a ChatMessage model (though that model is probably present in the sample code provided at the end of this sequence). That's work for a future followup.

Make sure that we have a nice UI for editing the room of existing chat rooms. For now, we'll rely on the existing admin console for Django, so, create and edit the chat/admin.py file:
'''
from django.contrib import admin
from chat.models import ChatRoom
 
admin.site.register(ChatRoom)
