from django.db import models
from django.contrib.auth.models import User

class Conversation(models.Model):
	page = models.URLField(primary_key=True)
	founder = models.ForeignKey(User)
	
	@models.permalink
	def get_absolute_url(self):
		return ('cmmntr.views.conversation', self.id)

class Comment(models.Model):
	conversation = models.ForeignKey(Conversation)
	user = models.ForeignKey(User)
	#parent = models.ForeignKey(Comment, null=True, blank=True) #Don't think I want to do this for now
	text = models.TextField()
