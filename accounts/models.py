from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

class Mentor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=100, verbose_name='이름')
    tel = models.CharField(max_length=20, verbose_name='전화번호')
    addr = models.CharField(max_length=100, verbose_name='주소')
    school = models.CharField(max_length=30, verbose_name='대학교')
    major = models.CharField(max_length=30, verbose_name='주전공')
    sub_major = models.CharField(max_length=30, blank=True, verbose_name='복수/부전공')
    grade = models.CharField(max_length=10, choices = (
                                            ('freshman','1학년'),
                                            ('sophomore','2학년'),
                                            ('junior','3학년'),
                                            ('senior','4학년'),
                                        ), verbose_name='학년')
    photo = ProcessedImageField(upload_to='menotor/profile/%Y/%m/%d', processors=[Thumbnail(300,300)], format='JPEG', options={'quality': 60}, verbose_name='프로필 사진')
    intro = models.TextField(verbose_name='소개글')
    hits = models.PositiveIntegerField(default = 0)

    class Meta:
        ordering = ['-id']