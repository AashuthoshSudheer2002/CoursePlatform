import cloudinary 
from decouple import config

CLOUDINARY_CLOUD_NAME = config('CLOUDINARY_CLOUD_NAME',default='dhdh8l7z')
CLOUDINARY_API_KEY = config('CLOUDINARY_API_KEY',default='1234567890')
CLOUDINARY_API_SECRET = config('CLOUDINARY_API_SECRET',default='1234567890')

def cloudinary_init():
    cloudinary.config( 
    cloud_name = CLOUDINARY_CLOUD_NAME, 
    api_key = CLOUDINARY_API_KEY, 
    api_secret = CLOUDINARY_API_SECRET,
    secure = True
    )

