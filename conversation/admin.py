from django.contrib import admin
from .models import ConversationMessage, Conversation

admin.site.register(ConversationMessage)
admin.site.register(Conversation)
