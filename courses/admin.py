from django.contrib import admin
from courses.models import *
from django.utils.html import format_html
from cloudinary import CloudinaryImage
# Register your models here.


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 1
    
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ['title', 'access', 'status']
    fields = ['title', 'access', 'status', 'image','display_image']
    list_filter  = ['access', 'status']
    search_fields = ['title', 'description']
    readonly_fields = ['display_image']

    def display_image(self,obj,*args,**kwargs):
        url = obj.image.url 
        cloudinary_id = str(obj.image)
        print(url ,cloudinary_id)
        cloudinary_html = CloudinaryImage(cloudinary_id).image(width=300) 
        return format_html(cloudinary_html)
    display_image.short_description = "Current Image"


