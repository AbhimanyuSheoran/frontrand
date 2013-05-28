from django.db import models
   
class BasicStat(models.Model):
    randomid=models.CharField(max_length=250)
    lenders=models.CharField(max_length=250)
    raised=models.CharField(max_length=250)
    livesch=models.CharField(max_length=250)
    repay=models.CharField(max_length=250)

def content_file_name(instance, filename):
    return '/'.join(['images','slider', instance.pid])

class Pictures(models.Model):
    image = models.ImageField(upload_to='images/slider/')
    caption = models.CharField(max_length=100)

class ImageWithThumbnail(models.Model):
    name = models.CharField(max_length = 255)
    detail= models.CharField(max_length = 255)
    image = models.ImageField(upload_to='faces/',max_length=500,blank=True,null=True)
    thumbnail = models.ImageField(upload_to='faces/',max_length=500,blank=True,null=True)
    testimonial = models.CharField(max_length = 300)
 
    def create_thumbnail(self):
        if not self.image:
            return
        from PIL import Image
        from cStringIO import StringIO
        from django.core.files.uploadedfile import SimpleUploadedFile
        import os
        THUMBNAIL_SIZE = (200,200)
        DJANGO_TYPE = self.image.file.content_type
        if DJANGO_TYPE == 'image/jpeg':
            PIL_TYPE = 'jpeg'
            FILE_EXTENSION = 'jpg'
        elif DJANGO_TYPE == 'image/png':
            PIL_TYPE = 'png'
            FILE_EXTENSION = 'png'
        image = Image.open(StringIO(self.image.read()))
        #if image.mode not in ('L', 'RGB'):
        #    image = image.convert('RGB')
        image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)
        # Save the thumbnail
        temp_handle = StringIO()
        image.save(temp_handle, PIL_TYPE)
        temp_handle.seek(0)
        # ImageField
        suf = SimpleUploadedFile(os.path.split(self.image.name)[-1],
                temp_handle.read(), content_type=DJANGO_TYPE)
        # Save SimpleUploadedFile into image field
        self.thumbnail.save('%s_thumbnail.%s'%(os.path.splitext(suf.name)[0],FILE_EXTENSION), suf, save=False)
        def save(self):
            self.create_thumbnail()
            super(ImageWithThumbnail, self).save()