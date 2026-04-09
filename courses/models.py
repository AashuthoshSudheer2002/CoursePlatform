from django.db import models
from cloudinary.models import CloudinaryField
from helpers.Cloudinary import _cloudinary

_cloudinary.cloudinary_init()


class AccessRequirement(models.TextChoices):
    ANYONE = "any", "Anyone"
    EMAIL_REQUIRED = "email", "Email required"

class PublishStatus(models.TextChoices):
    PUBLISHED = "publish", "Published"
    COMING_SOON = "soon", "Coming Soon"
    DRAFT = "draft", "Draft"

class Course(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    image = CloudinaryField('image', blank=True, null=True)
    public_id = models.CharField(max_length=130, blank=True, null=True, db_index=True)
    access = models.CharField(
        max_length=5, 
        choices=AccessRequirement.choices,
        default=AccessRequirement.EMAIL_REQUIRED
    )
    status = models.CharField(
        max_length=10, 
        choices=PublishStatus.choices,
        default=PublishStatus.DRAFT
        )
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def is_published(self):
        return self.status == PublishStatus.PUBLISHED

    @property
    def admin_image(self):
        if not self.image:
            return ""
        image_options = {
            "width": 150,
            "height": 150,
        }
        return self.image.build_url(**image_options)
    
    
    def retrieve_image_thumbnail(self , as_html=False):
        if not self.image:
            return ""
        image_options = {
            "width": 150,
            "height": 150,
        }
        if as_html:
            #CloudinaryImage(self.image.public_id).image(**image_options) --- IGNORE ---
            return self.image.image(**image_options)
        url = self.image.build_url(**image_options)
        return url
class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    order = models.PositiveIntegerField(default=0)
    thumbnail = CloudinaryField('thumbnail', blank=True, null=True)
    video = CloudinaryField('video', blank=True, null=True,resource_type='video')
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10, 
        choices=PublishStatus.choices,
        default=PublishStatus.PUBLISHED
        )
    class Meta:
        ordering = ['order','timestamp']