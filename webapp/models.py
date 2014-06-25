from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Contributor(models.Model):
    """
    Fields are:

    user: This is the Default django user object

    contact: This is the contact number of the user. It must be an integer.

    picture: The profile picture of the contributor. may be jpg or jpeg or png
or bmp.

    validation_docs: The Valid certificate of the user stating his educational
qualifications.
    """
    user = models.OneToOneField(User)
    # Addition info
    contact = models.CharField(max_length=12, blank=True)
    picture = models.ImageField(upload_to='profile_image', blank=True)
    validation_docs = models.FileField(upload_to='validation_docs',
                                       blank=False)

    def __unicode__(self):
        return self.user.username


class Language(models.Model):
    language = models.CharField(max_length=100, blank=False)

    def __unicode__(self):
        return u"%s" % (self.language)


class Reviewer(models.Model):
    """
    Fields are:

    user: This is the Default django user object.

    contact: This is the contact number of the user. It must be an integer.

    picture: The profile picture of the contributor. may be jpg or jpeg or png
or bmp.
    """
    user = models.OneToOneField(User)
    # Addition info
    contact = models.CharField(max_length=12, blank=True)
    picture = models.ImageField(upload_to='profile_image', blank=True)

    def __unicode__(self):
        return self.user.username


class Class(models.Model):
    """
    Fields are:

    class_number: This will be class number like first, second .. eight ..
tenth.

    remark: This is the remark given by the teacher.
    """
    class_number = models.IntegerField(default=1)
    remark = models.TextField()

    def __unicode__(self):
        return u"%d" % (self.class_number)


class Subject(models.Model):
    """
    Fields are:

    contributor: This field is a foreign key to the Contributor class. This is
used to refer to the contributors who are already signed up.

    name: This field is the name of the subject,the contributor is specialized
in.

    topic: The subject of the topic the contibutor is going to contribute.

    class_number: This may be the class number like first, second .. eight ..
tenth for which the contributor is uploading his files.

    pdf: The contributor has to upload the files.This field describes that the
uploaded file must be a pdf file.

    video: The contributor has to upload the files.This field describes that
the uploaded file must be a video. May be mp4.

    animation: The contributor has to upload the files.This field describes
that the uploaded file must be an animation file. This may be gif.

    pdf_url: If the size of the uploaded file is high contributor can just
mention the url of the file. This field is used to mention the url of the file.

    video_URL: If the size of the uploading video is greater than the limited
size, contributor can just mention the url of the video. This field is used to
mention the url of the video.

    animation_url: If the size of the uploaded Animation is greater than the
limited size, contributor can just mention the url of the animation. This
field is used to mention the  url of the animation.

    uploaded_on: This field is used to obtain the date on which the file is
uploaded by the contributor. This must be the date field.

    summary: This is the Summary given by the contributor about the specified
topic of the specified subject including when to use and how to use.

    rating: The field indicates the rating given by the reviewer for his
uploaded files. This must be an integer and default value is 0.

    review: This field indicate the number of reviews made by the reviewers.
This This must be an integer and default value is 0.

    language: This field is a foreign key to the Language class. This is
used to refer to the language in which the contributor is contributing.


    """
    contributor = models.ForeignKey(Contributor)
    name = models.CharField(
        max_length=50,
        validators=[RegexValidator(regex=r'^[a-zA-Z ]*$',
                    message='Special Characters are not allowed',
                    code='nnomatch')])
    topic = models.CharField(
        max_length=200,
        validators=[RegexValidator(regex=r'^[a-zA-Z ]*$',
                    message='Special Characters are not allowed',
                    code='nnomatch')])
    class_number = models.ForeignKey(Class)
    pdf = models.FileField(upload_to='pdf', blank=True)
    video = models.FileField(upload_to='video', blank=True)
    animation = models.FileField(upload_to='animation', blank=True)
    pdf_url = models.URLField(blank=True)
    video_url = models.URLField(blank=True)
    animation_url = models.URLField(blank=True)
    uploaded_on = models.DateField(auto_now=True)
    summary = models.TextField(blank=False)
    rating = models.IntegerField(default=0)
    review = models.IntegerField(default=0)
    reviewer = models.ManyToManyField(Reviewer)
    language = models.ForeignKey(Language)

    def __unicode__(self):
        return u"%s : %s" % (self.name, self.topic)

    def increment_review(self):
        self.review += 1
        self.save()


class Contact(models.Model):
    """
    Fields are:

    name: This field indicates the name of the non-user who wants to suggest
any modifications.

    email: This fied indicates the mail-id of the non-user.

    message: This field describes the modifications suggested by the non-user,
if any.
"""
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=False)
    message = models.TextField(max_length=500)

    def __unicode__(self):
        return u"%s - %s" % (self.name, self.email)


class Faq(models.Model):
    """
    Fields are:

    question: This field descibes the frequently asked questions.

    answer: This field describes the answers for the frequently asked
questions.
    """
    question = models.TextField(max_length=500)
    answer = models.TextField()

    def __unicode__(self):
        return self.question


class Comment(models.Model):
    """
    Fields are:

    subject: This field indicates the subject on which comments are arrived.
This field is the foreign key to the Subject class.

    user: This field indicates the reviewer who has commented on the uploaded
files of the contributor. This is a foreign key to the Reviewer class.

    comment: This describes the actual comments of the reviewer.

    submit_date: Submit_date field tells us when the comment was submitted,
at which time and on which date. This uses DateTime field.
    """
    subject = models.ForeignKey(Subject)
    user = models.ForeignKey(Reviewer)
    comment = models.TextField(max_length=1000)
    submit_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.comment
