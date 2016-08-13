from django.contrib import admin
from OnlineEditor.models import OnlineEditorModel

# Register your models here.
admin.site.unregister(OnlineEditorModel)
admin.site.register(OnlineEditorModel)
