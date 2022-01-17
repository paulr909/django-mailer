from django.contrib import admin

from mailinglist.models import MailingList, Message, Subscriber

admin.site.register(Message)
admin.site.register(MailingList)
admin.site.register(Subscriber)
