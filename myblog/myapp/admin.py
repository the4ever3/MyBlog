from django.contrib import admin
from .models import BlogPost, PersonalInfo, MyExpertise, Skills, Languages, Expertise, Education, Contact

# Register your models here.

admin.site.register(BlogPost)
admin.site.register(PersonalInfo)
admin.site.register(MyExpertise)
admin.site.register(Skills)
admin.site.register(Languages)
admin.site.register(Expertise)
admin.site.register(Education)
admin.site.register(Contact)


# class BlogPost(admin.ModelAdmin):
#     list_display = ('title', 'author', 'published_date')
#     search_fields = ('title', 'author__name')
#
# class PersonalInfo(admin.ModelAdmin):
#     list_display = ('name', 'last_name', 'email', 'phone')
#     search_fields = ('name', 'last_name', 'email')