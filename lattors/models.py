from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from django.conf import settings

class Mentors(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,blank=True, null=True)
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


class Mentee(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,blank=True, null=True)
    name = models.CharField(max_length=100, verbose_name='이름')
    tel = models.CharField(max_length=20, verbose_name='전화번호')
    addr = models.CharField(max_length=100, verbose_name='주소')
    school = models.CharField(max_length=30, verbose_name='고등학교')
    school_type = models.CharField(max_length=20, choices = (
                                                ('일반','일반 인문계 고등학교'),
                                                ('외고','외국어 고등학교'),
                                                ('과고','과학 고등학교'),
                                                ('자사고','자율형 사립고등학교'),
                                                ('자율고','자율형 공립고등학교'),
                                                ('실업계','실업계/전문 고등학교'),
                                            ), verbose_name='학교 유형')
    grade = models.CharField(max_length=10, choices = (
                                            ('first','1학년'),
                                            ('second','2학년'),
                                            ('third','3학년'),
                                        ), verbose_name='학년')
    school_expect = models.CharField(max_length=30, verbose_name='희망 대학교')
    major_expect = models.ManyToManyField('Major', verbose_name='희망 전공')
    photo = ProcessedImageField(blank=True, upload_to='mentee/profile/%Y/%m/%d', processors=[Thumbnail(300,300)], format='JPEG', options={'quality': 60}, verbose_name="프로필 사진")
    intro = models.TextField(verbose_name='소개글')

    class Meta:
        ordering = ['-id']


class Major(models.Model):
    major = models.CharField(max_length=30, verbose_name='전공', unique=True)

    def __str__(self):
        return self.major