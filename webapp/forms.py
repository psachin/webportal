from django import forms
from django.contrib.auth.models import User
from django.contrib import messages

#import the models here
from models import Contributor, Reviewer, Class
from models import Subject, Comment, Language, Contact


class ContactForm(forms.ModelForm):
    """
    Fields are:

    name: This field tells the name of the student contacting us.

    email: This field tells the email of the student contacting us.

    message: This field tells the message of the student contacting us
    """
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your name*.'}),
        help_text="Enter your name.",
        required=True)
    email = forms.EmailField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter valid email*.'}),
        help_text="Enter Email.",
        required=True)
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Please write your message*.',
            'rows': 4}),
        help_text="Please write your message.",
        required=True)

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']


class UserForm(forms.ModelForm):
    """
    Fields are:

    username: This field tells the user who sign in.

    first_name: This field tells the First name of the user.

    last_name: This field tells the Last name of the user.

    email: Email field tells the mail id of the user who sign in.

    password: This tells the user to set his own password.
    """
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username  to login*.'}),
        help_text="",
        required=True,
        error_messages={'required': 'Username is required.'})
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'First name*.'}),
        help_text="",
        required=True,
        error_messages={'required': 'First name is required.'})
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Last name*.'}),
        help_text="",
        required=True,
        error_messages={'required': 'Last name is required.'})
    email = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Valid email*.'}),
        help_text="",
        required=True,
        error_messages={'required': 'Valid Email address is required.'})
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password*.'}),
        help_text="",
        required=True,
        error_messages={'required': 'Password is missing.'})

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password',)


class ContributorForm(forms.ModelForm):
    """
    Fields are:

    contact: This is the contact number of the user. It must be an integer.

    validation_docs: The Valid certificate of the user stating his
educational qualifications.

    picture: The profile picture of the contributor. may be jpg or jpeg or
png or bmp.
    """
    contact = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contribter contact number.'}),
        help_text="",
        required=False,
        error_messages={'required': 'Last name is required.'})
    validation_docs = forms.FileField(
        label='Validation file.',
        widget=forms.FileInput(),
        help_text='Upload validation file.',
        required=False)
    picture = forms.ImageField(
        label='Profile picture',
        widget=forms.FileInput(attrs={
            'placeholder': 'Contributor picture.'}),
        required=False)

    class Meta:
        model = Contributor
        fields = ('picture', 'contact', 'validation_docs')

    def clean_validtion_docs_file(self):
        """Limit doc_file upload size."""
        if self.cleaned_data['validation_docs']:
            validation_docs = self.cleaned_data['validation_docs']
            return validation_docs
        else:
            raise forms.ValidationError("Not a valid file!")


class ReviewerForm(forms.ModelForm):
    """
    Fields are:

    picture: The profile picture of the Reviewer. may be jpg or jpeg or png
or bmp.

    contact: This is the contact number of the user. It must be an integer.
    """
    error_css_class = 'error'
    required_css_class = 'required'

    picture = forms.ImageField(
        label='Profile picture',
        widget=forms.FileInput(attrs={
            'placeholder': 'Reviewer picture.'}),
        required=False)
    contact = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Reviewer contact number.'}),
        help_text="",
        required=False,
        error_messages={'required': 'Last name is required.'})

    class Meta:
        model = Reviewer
        fields = ('picture', 'contact')


class ContributorUploadForm(forms.ModelForm):
    """
    Fields are:

    class_number: This will be class number like first, second .. eight ..
tenth.

    name: This field is the name of the subject,the contributor is specialized
in.

    topic: The subject of the topic the contibutor is going to contribute.

    pdf: The contributor has to upload the files.This field describes that the
uploaded file must be a pdf file.

    video: The contributor has to upload the files.This field describes that
the uploaded file must be a video. May be mp4.

    animation: The contributor has to upload the files.This field describes
that the uploaded file must be an animation file. This may be gif.

    summary: This is the summary given by the contributor about the specified
topic of the specified subject including when to use and how to use.
    """
    language = forms.ModelChoiceField(
        label='Language',
        cache_choices=True,
        widget=None,
        queryset=Language.objects.all(),
        empty_label=None,
        help_text="",
        required=True,
        error_messages={'required': 'Language is required'})
    class_number = forms.ModelChoiceField(
        label='Class',
        cache_choices=True,
        widget=None,
        queryset=Class.objects.all(),
        empty_label=None,
        help_text="",
        required=True,
        error_messages={'required': 'Class is required'})
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Subject name*.'}),
        help_text="",
        required=True,
        error_messages={'required': 'Subject name is required.'})
    topic = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Subject topic*.'}),
        help_text="",
        required=True,
        error_messages={'required': 'Subject topic is required.'})
    pdf = forms.FileField(
        label='pdf file.',
        widget=forms.FileInput(),
        help_text='Upload pdf file.',
        required=False)
    video = forms.FileField(
        label='video file.',
        help_text='Upload video file.',
        required=False)
    animation = forms.FileField(
        label='animations file.',
        widget=forms.FileInput(),
        help_text='Upload animations file.',
        required=False)
    summary = forms.CharField(
        label='Summary',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Summary for the uploaded documents.'}),
        help_text="",
        required=True,
        error_messages={'required': 'Summary is required.'})

    class Meta:
        model = Subject
        fields = ['language', 'class_number', 'name', 'topic', 'pdf', 'video',
                  'animation', 'summary']

    def clean_pdf(self):
        """Upload a valid."""
        if self.cleaned_data['pdf']:
            pdf = self.cleaned_data['pdf']
            print pdf.content_type.split('/')[1]
            if pdf.content_type.split('/')[1] == "pdf":
                if pdf._size/(1024*1024) <= 20:  # < 20MB
                    return pdf
                else:
                    raise forms.ValidationError("PDF file max. size is 20MB.")
            else:
                    raise forms.ValidationError("Not a valid pdf file!")

    def clean_video(self):
        """Limit doc_file upload size."""
        if self.cleaned_data['video']:
            video = self.cleaned_data['video']
            if video.content_type.split('/')[1] in ("mp4", "x-matroska",
                                                    "x-msvideo", "x-flv"):
                if video._size/(1024*1024) <= 200:  # < 100MB
                    return video
                else:
                    raise forms.ValidationError("File max. size is 100MB.")
            else:
                raise forms.ValidationError("Not a valid video file")

    def clean_animation(self):
        """Limit doc_file upload size."""
        if self.cleaned_data['animation']:
            animation = self.cleaned_data['animation']
            if animation.content_type.split('/')[1] == "x-shockwave-flash":
                if animation._size/(1024*1024) <= 10:  # < 10MB
                    return animation
                else:
                    raise forms.ValidationError("File max. size is 10MB.")
            else:
                raise forms.ValidationError("Not a valid file!")


class CommentForm(forms.ModelForm):
    """
    Field  is:

    comment: This field describes the comment form which takes maximum length
of 1000 characters. The comment is made by the reviewer.
    """
    comment = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'rows': '3'}),
        help_text="",
        required=False,)

    class Meta:
        model = Comment
        fields = ['comment']
