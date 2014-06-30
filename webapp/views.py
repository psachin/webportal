from django.shortcuts import HttpResponse, render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext, loader, Context
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

# import the models here

from django.contrib.auth.models import User
from webapp.models import Contributor, Reviewer, Subject ,Comment, Language,Class

# import the forms here
from webapp.forms import ContributorForm, ReviewerForm, UserForm
from webapp.forms import ContactForm, ContributorUploadForm, CommentForm


def index(request):
    """
    Argument:

    `request`: Request from client.

    This function takes the request of client and direct it to home page.
    """
    context = RequestContext(request)
    latest_uploads_all = Subject.objects.all()
    num_class = Class.objects.all()
    num_subject = Subject.objects.values_list('name', flat=True).distinct()
    filter_review = Subject.objects.filter(review__gte=3)
    latest_uploads = filter_review.order_by('-uploaded_on')[:5]
    count = len(latest_uploads_all)
    count_subject = len(num_subject)
    count_class = len(num_class)
    context_dict = {
        'latest_uploads': latest_uploads,
        'count': count,
        'count_subject': count_subject,
        'count_class': count_class
    }
    return render_to_response("webapp/index.html", context_dict, context)


def about(request):
    """About page.

    Argument:

    `request`: Request from client This function takes the request of
    the client and direct it to the page consisting of the description
    about the site.
    """

    context = RequestContext(request)
    return render_to_response('about.html', context)


def contact(request):
    """Contact us page.

    Arguments: 

    `request`: Request from the client.
  
    This function takes the request of the client and direct it to the
    contact us page.
    """
    context = RequestContext(request)

    if request.POST:
        contactform = ContactForm(data=request.POST)
        if contactform.is_valid():
            contactform = contactform.save(commit=True)
            email_subject = "[aakashschooleducation.org] Contact Us"
            email_message = "Sender Name: " + contactform.name + "\n \
\n" + contactform.message
            #send_mail(email_subject, email_message,
            #          contactform.email,
            #          [
            #              'iclcoolster@gmail.com',
            #              'Aakashprojects.iitb@gmail.com',
            #              'aakashmhrd@gmail.com',
            #          ],
            #          fail_silently=False)
            messages.success(request, "Thank you for your reply. We\
will get back to you soon.")
        else:
            print contactform.errors
            messages.error(request, "One or more fields are required or not \
            valid.")
    else:
        contactform = ContactForm()

    context_dict = {'contactform': contactform}
    return render_to_response('contact.html', context_dict, context)


def userlogin(request):
    """
    Argument:

    `request`: Request from the user to login.

    This function takes the request of the user and direct it to the
    login page.
    
    """
    context = RequestContext(request)
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                # Is the account active? It could have been disabled.
                if user.is_active:
                    # If the account is valid and active, we can log the
                    # user in.
                    # We'll send the user back to the homepage.
                    u = User.objects.get(username=user.username)
                    if Contributor.objects.filter(user=u):
                        login(request, user)
                        return HttpResponseRedirect('/contributor/profile/')
                    elif Reviewer.objects.filter(user=u):
                        login(request, user)
                        return HttpResponseRedirect('/reviewer/profile/')
                    elif user.username == 'admin':
                        login(request, user)
                        return HttpResponseRedirect('/admin')
                    else:
                        # An inactive account was used - no logging in!
                        messages.info(request, "Your account is disabled.")
                        return render_to_response('webapp/login.html', context)
            else:
                # Bad login details were provided. So we can't log the user in.
                messages.error(request, "Bad login!")
                return render_to_response('webapp/login.html', context)
        else:
            return render_to_response('webapp/login.html', context)

def password_change(request):
    context = RequestContext(request)
    user = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        if user.check_password(request.POST['old_pwd']):
            if request.POST['new_pwd'] == request.POST['new_again_pwd']:
                user.set_password(request.POST['new_pwd'])
		user.save()
                messages.success(request, "Password Changed")
		return render_to_response('password_change.html',context)
            else:
                messages.error(request, "Passwords doesn't match")
		return render_to_response('password_change.html',context)		
        else:
            messages.error(request, "Incorrect Password")
	    return render_to_response('password_change.html',context)
    else:
        return render_to_response('password_change.html', context)
    

def contributor_profile(request):
    """
    Arguments:

    `request`: Request from user

    This function takes the request of user and direct it to profile page.
    """
    context = RequestContext(request)
    contributor = Contributor.objects.get(user=request.user)
    filter_class = Subject.objects.values_list(
        'class_number__class_number',
        flat=True).order_by('class_number')
    uploads = filter_class.filter(contributor__user=request.user).distinct()
    context_dict = {
        'uploads': uploads,
        'contributor': contributor
    }
    return render_to_response('contributor.html', context_dict, context)


def contributor_profile_subject(request, class_num):
    """
    Arguments:

    `request`: Request from user

    `class_num`: Class in which the logged in contributor has contributed

    This function takes the request of user and direct it to profile
    page which consists of his contributions in a specific class.

    """
    context = RequestContext(request)
    contributor = Contributor.objects.get(user=request.user)
    filter_sub = Subject.objects.values_list('name', flat=True).distinct()
    filter_class = filter_sub.filter(class_number__class_number=class_num)
    uploads = filter_class.filter(contributor__user=request.user)
    uploads = uploads.order_by('name')
    context_dict = {
        'uploads': uploads,
        'class_num': class_num,
        'contributor': contributor
    }
    return render_to_response('contributor_subject.html', context_dict,
                              context)


def contributor_profile_topic(request, class_num, sub):
    """
    Arguments:

    `request`: Request from user

    `class_num`: Class in which the logged in contributor has contributed

    `sub`: Subject in which the logged in contributor has contributed

    This function takes the request of user and direct it to profile
    page which consists of his contributions in a specific subject of a
    specific class.

    """
    context = RequestContext(request)
    contributor = Contributor.objects.get(user=request.user)
    filter_class = Subject.objects.filter(class_number__class_number=class_num)
    filter_sub = filter_class.filter(name=sub)
    uploads = filter_sub.filter(contributor__user=request.user)
    uploads = uploads.order_by('topic')
    context_dict = {
        'uploads': uploads,
        'class_num': class_num,
        'sub': sub,
        'contributor': contributor}
    return render_to_response('contributor_topic.html', context_dict, context)


def contributor_profile_comment(request, class_num, sub, topics, id):
    """
    Arguments:

    `request`: Request from user.

    `class_num`: Class in which the logged in contributor has contributed.

    `sub`: Subject in which the logged in contributor has contributed.

    `topics`: Subject topic in which the logged in contributor has
    contributed.

    This function takes the request of user and direct it to profile
    page which consists of his comments of reviewer on a specific
    subject of a specific class. 

    """
    context = RequestContext(request)
    contributor = Contributor.objects.get(user=request.user)
    comment = Comment.objects.filter(subject_id=id).order_by('-submit_date')
    context_dict = {
        'comment': comment,
        'class_num': class_num,
        'sub': sub,
        'topics': topics,
        'id': id,
        'contributor': contributor,
    }
    return render_to_response('contributor_comment.html', context_dict,
                              context)


def contributor_profile_topic_detail(request, class_num, sub, topics, id):
    """
    Arguments:

    `request`: Request from user.

    `class_num`: Class in which the logged in contributor has contributed.

    `sub`: Subject in which the logged in contributor has contributed.

    `topics`: Subject topic in which the logged in contributor has
    contributed.

    `id`: Id of the subject in which the logged in contributor has
    contributed.

    This function takes the request of user and direct it to profile page which
    consists of his comments of reviewer on a specified topic of a subject of a
    specific class.
    
    """
    context = RequestContext(request)
    contributor = Contributor.objects.get(user=request.user)
    subject = Subject.objects.get(id=id)
    context_dict = {
        'subject': subject,
        'class_num': class_num,
        'sub': sub,
        'contributor': contributor,
        'topics': topics,
        'id': id,
    }
    return render_to_response('contributor_topic_detail.html',
                              context_dict, context)

def topic(request,class_num,sub,topics,id):
    """
    Arguments:

    `request`: Request from user.

    `class_num`: Class in which the logged in contributor has
    contributed.

    `sub`: Subject in which the logged in contributor has contributed.

    `topics`: Subject topic in which the logged in contributor has
    contributed.

    `ID` : Id of the subject in which the logged in contributor has contributed.

    This function takes the request of user and direct it to profile
    page which consists of details of a specified topic of a subject
    of a specific class.

    """
    context = RequestContext(request)
    subject = Subject.objects.get(id=id)
    context_dict = {'subject': subject, 'class_num':class_num, 'sub':sub,'topics':topics,'id':id}
    return render_to_response('topic.html', context_dict, context)


def reviewer_profile_topic_detail(request, class_num, sub, topics, id):
    """
    Arguments:

    `request`: Request from user.

    `class_num`: Class in which the logged in contributor has
    contributed.

    `sub`: Subject in which the logged in contributor has contributed.

    `topics`: Subject topic in which the logged in contributor has
    contributed.

    `id`: Id of the subject in which the logged in contributor has
    contributed.

    This function takes the request of user and direct it to profile
    page which consists of his comments of reviewer on a specified topic
    of a subject of a specific class.
    
    """
    context = RequestContext(request)
    reviewer = Reviewer.objects.get(user=request.user)
    subject = Subject.objects.get(pk=id)
    context_dict = {
        'subject': subject,
        'class_num': class_num,
        'sub': sub,
        'reviewer': reviewer,
        'topics': topics,
        'id': id,
    }
    return render_to_response('reviewer_topic_detail.html',
                              context_dict, context)


@login_required
def reviewer_profile(request):
    """
    Arguments:

    `request`: Request from user.

    This function takes the request of user and directs it to the profile page.
    
    """
    context = RequestContext(request)
    reviewer = Reviewer.objects.get(user=request.user)
    filter_class = Subject.objects.values_list(
        'class_number__class_number',
        flat=True).order_by('class_number')
    uploads = filter_class.filter(review__lt=3).distinct()
    context_dict = {'uploads': uploads, 'reviewer': reviewer}
    return render_to_response("reviewer.html", context_dict, context)


def reviewer_profile_subject(request, class_num):
    """
    Arguments:

    `request`: Request from user.

    `class_num` : Class in which the contributor has contributed.

    This function takes the request of user and direct it to the
    profile page which consists of the contributor's contributions in a
    specific class.
    """
    context = RequestContext(request)
    reviewer = Reviewer.objects.get(user=request.user)
    filter_sub = Subject.objects.values_list('name', flat=True).distinct()
    filter_class = filter_sub.filter(class_number__class_number=class_num)
    uploads = filter_class.filter(review__lt=3).order_by('name')
    context_dict = {
        'uploads': uploads,
        'class_num': class_num,
        'reviewer': reviewer,
    }
    return render_to_response('reviewer_subject.html', context_dict, context)


def reviewer_profile_topic(request, class_num, sub):
    """
    Arguments:

    `request`: Request from user.

    `class_num` : Class in which the contributor has contributed.

    `sub`: subject in which the contributor has contributed.

    This function takes the request of user and directs it to the
    profile page which consists of the contributor's contributions in a
    specific subject of a specific class.
    """
    context = RequestContext(request)
    reviewer = Reviewer.objects.get(user=request.user)
    if request.POST:
        print request
        subject = get_object_or_404(Subject, id=request.POST['id'])
        subject.increment_review()
        subject.reviewer.add(reviewer)
        print "reviewer has reviewed"
        print subject.review
        print subject.id
    filter_sub = Subject.objects.filter(class_number__class_number=class_num)
    uploads = filter_sub.filter(name=sub).filter(review__lt=3)
    uploads = uploads.order_by('topic')
    context_dict = {
        'uploads': uploads,
        'class_num': class_num,
        'sub': sub,
        'reviewer': reviewer,
    }
    return render_to_response('reviewer_topic.html', context_dict, context)


def reviewer_profile_comment(request, class_num, sub, topics, id):
    """
    Arguments:

    `request`: Request from user.

    `class_num`: Class in which the contributor has contributed.

    `sub`: Subject in which the contributor has contributed.

    `topics`: Topic on which reviewer commented.

    `id`: Id of the reviewer.

    This function takes the request of user and directs it to the
    profile page which consists of the contributor's contributions in a
    specific subject of a specific class.
    
    """
    context = RequestContext(request)
    comment = Comment.objects.filter(subject_id=id).order_by('-submit_date')
    reviewer = Reviewer.objects.get(user=request.user)
    if request.method == 'POST':
        print "we have a new comment"
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comments = comment_form.save(commit=False)
            subject = Subject.objects.get(pk=id)
            comments.subject = subject
            comments.user = reviewer
            comments.save()
            url = reverse('webapp.views.reviewer_profile_comment', kwargs={
                'class_num': class_num, 'sub': sub, 'topics': topics, 'id': id}
            )
            return HttpResponseRedirect(url)
        else:
            if comment_form.errors:
                print comment_form.errors
    else:
        comment_form = CommentForm()
        context_dict = {
            'comment_form': comment_form,
            'comment': comment,
            'reviewer': reviewer,
        }
        return render_to_response("reviewer_comment.html",
                                  context_dict, context)


def reviewer_past_approvals(request):
    """
    Argument:

    `request`: Request from contributor to sign up.

    This function takes the request of user and directs it to the
    profile page which consists of the reviewer's past approvals.
    
    """
    context = RequestContext(request)
    reviewer = Reviewer.objects.get(user=request.user)
    subject = Subject.objects.all().order_by('-uploaded_on')
    past_approvals = list()
    count = 0
    for i in subject:
       if count == 10:
           break
       if reviewer in i.reviewer.all():
          past_approvals.append(i)
          count += 1
    context_dict = {'past_approvals': past_approvals, 'reviewer': reviewer}
    return render_to_response("reviewer_past_approvals.html",
                              context_dict, context)


def topic(request, class_num, sub, topics, id):
    """
    Arguments:

    `request`: Request from user.

    `class_num`: Class in which the logged in contributor has
    contributed.

    `sub`: Subject in which the logged in contributor has contributed.

    `topics`: Subject topic in which the logged in contributor has
    contributed.

    `id`: Id of the subject in which the logged in contributor has
    contributed.

    This function takes the request of user and direct it to profile
    page which consists of details of a specified topic of a subject of a
    specific class.
    
    """
    context = RequestContext(request)
    subject = Subject.objects.get(id=id)
    context_dict = {'subject': subject, 'class_num': class_num,
                    'sub': sub, 'topics': topics, 'id': id}
    return render_to_response('topic.html', context_dict, context)


def contributor_signup(request):
    """
    Argument:

    `request`: Request from contributor to sign up.

    This function is used for a new contributor to sign up.

    `Usage`: ::

        # Create an instance for UserForm() and ContributotForm()
        user_form = UserForm(data=request.POST)
        contributor_form = ContributorForm(data=request.POST)
        if user_form.is_valid() and contributor_form.is_valid():
            user = user_form.save()
            # do stuff
        else:
            # do stuff
    """
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        print "we have a request to register"
        user_form = UserForm(data=request.POST)
        contributor_form = ContributorForm(data=request.POST)
        if user_form.is_valid() and contributor_form.is_valid():
            user = user_form.save()
            print "Forms are Valid"
            print user.username
            print user.first_name
            user.set_password(user.password)
            user.is_active = False
            user.save()
            contributor = contributor_form.save(commit=False)
            contributor.user = user
            if 'picture' in request.FILES:
                contributor.picture = request.FILES['picture']
            if 'validation_docs' in request.FILES:
                contributor.validation_docs = request.FILES['validation_docs']
            contributor.save()
            registered = True
            email_subject = "New Contributor has registered"
            email_message = """
New Contributor has registered.
Details:
Name:""" + user.first_name + """  """ + user.last_name + """"
Email:""" + user.email + """
Waiting for your your approval"""
# send_mail(email_subject, email_message, 'khushbu.ag23@gmail.com',
#           ['pri.chundawat@gmail.com'],fail_silently=False)
            messages.success(
                request,
                "Form successfully submitted. Waiting for activation \
from admin.")
            return HttpResponseRedirect(reverse('webapp.views.contributor_signup'))
        else:
            if contributor_form.errors or user_form.errors:
                print user_form.errors, contributor_form.errors
    else:
        contributor_form = ContributorForm()
        user_form = UserForm()
    context_dict = {
        'user_form': user_form,
        'contributor_form': contributor_form,
        'registered': registered,
    }
    return render_to_response('webapp/contributor_signup.html',
                              context_dict, context)


def reviewer_signup(request):
    """
    Argument:

    `request`: Request from reviewer to sign up.

    This function is used for a new revieweer to sign up.

    """
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        print "we have a request to register"    
        user_form = UserForm(data=request.POST)
        reviewer_form = ReviewerForm(data=request.POST)
        if user_form.is_valid() and reviewer_form.is_valid():
            user = user_form.save()
            print "Forms are Valid"
            print user.username
            print user.first_name
            user.set_password(user.password)
            user.is_active = False
            user.save()
            reviewer = reviewer_form.save(commit=False)
            reviewer.user = user
            if 'picture' in request.FILES:
                reviewer.picture = request.FILES['picture']
            reviewer.save()                       
            registered = True
            email_subject="New reviewer has registered"
	    email_message="""
New reviewer has registered.
    	
Details:
Name:""" + user.first_name + """  """ + user.last_name + """"
Email:""" + user.email + """
Waiting for your your approval"""
            #send_mail(email_subject, email_message, 'khushbu.ag23@gmail.com', ['pri.chundawat@gmail.com'],fail_silently=False)

            messages.success(request,"form successfully submitted. Waiting for activation  from admin.")
            return HttpResponseRedirect(reverse('webapp.views.reviewer_signup'))
        else:
            if reviewer_form.errors or user_form.errors:
                print user_form.errors, reviewer_form.errors
    else:
        reviewer_form = ReviewerForm()
        user_form = UserForm()	
    context_dict = {'user_form': user_form,
                        'reviewer_form': reviewer_form,
                        'registered': registered}
    return render_to_response('webapp/reviewer_signup.html', context_dict, context)

def user_logout(request):
    """
    Argument:

    `request`: Request from user to log out

    This function is used for logging out.

    """
    context = RequestContext(request)
    logout(request)
    return HttpResponseRedirect('/')


def commentpost(request):
    """
    Argument:

    `request`: This redirects the comments to comments.html page.
    """
    return render_to_response('templates/comments.html')


def contributor_upload(request):
    """
    Argument:

    `request`: Request from contributor for a new upload.

     This function is used to upload a new file by contributor.

    """
    context = RequestContext(request)
    uploaded = False
    if request.POST:
        print "we have a request for upload by the contributor"
        contributor_upload_form = ContributorUploadForm(request.POST,
                                                        request.FILES)

        if contributor_upload_form.is_valid():
            print "Forms is/are valid"
            subject = contributor_upload_form.save(commit=False)
            if ('pdf' not in request.FILES
                and 'animation' not in request.FILES
                    and 'video' not in request.FILES):
                # Bad upload details were provided.
                messages.error(request, "need to provide atleast one upload")
                contributor_upload_form = ContributorUploadForm()
                context_dict = {
                    'contributor_upload_form': contributor_upload_form,
                    'uploaded': uploaded}
                return render_to_response("upload.html", context_dict, context)
            else:
                if 'pdf' in request.FILES:
                    subject.pdf = request.FILES['pdf']
                if 'video' in request.FILES:
                    subject.video = request.FILES['video']
                if 'animation' in request.FILES:
                    subject.animation = request.FILES['animation']
            contributor = Contributor.objects.get(user=request.user)
            subject.contributor = contributor

            subject.save()
            uploaded = True
            contributor_name = request.user.username
            return HttpResponseRedirect('/contributor/profile/')
        else:
            if contributor_upload_form.errors:
                print contributor_upload_form.errors
    else:
        # empty form
        contributor_upload_form = ContributorUploadForm()

    context_dict = {
        'contributor_upload_form': contributor_upload_form,
        'uploaded': uploaded
    }

    return render_to_response("upload.html", context_dict, context)


@login_required
def contributor_profile_edit(request):
    """
    Argument:

    `request`: Request form contributor to edit his profile.

    Edit user's/Coordinators profile.

    """
    context = RequestContext(request)
    print request.user
    user = get_object_or_404(User, username=request.user)
    old_username = user.username
    print user.first_name
    print user.last_name
    contributor = get_object_or_404(Contributor, user=request.user)
    if request.method == 'POST':
        print "We've a request to register"
        contributorform = ContributorForm(data=request.POST,
                                          instance=contributor)
        userform = UserForm(data=request.POST, instance=user)
        if contributorform.is_valid() and userform.is_valid():
            print "Forms are Valid"
            user = userform.save(commit=False)
            if old_username != user.username:
                messages.error(request, 'Username cant be changed')
                context_dict = {
                    'contributorform': contributorform,
                    'userform': userform
                }
                return render_to_response('contributor_profile_edit.html',
                                          context_dict, context)
            user.set_password(user.password)
            user.save()
            contributor = contributorform.save(commit=False)
            if 'picture' in request.FILES:
                contributor.picture = request.FILES['picture']
            contributor.user = User.objects.get(username=user.username)
            contributor.save()
            messages.success(request, "Profile updated successfully.")
        else:
            if contributorform.errors or userform.errors:
                print contributorform.errors, userform.errors
    else:
        contributorform = ContributorForm(instance=contributor)
        userform = UserForm(instance=user)
    context_dict = {'contributorform': contributorform, 'userform': userform}
    return render_to_response('contributor_profile_edit.html',
                              context_dict, context)


@login_required
def reviewer_profile_edit(request):
    """
    Argument:

    `request`: Request from reviewer to edit his profile.

    Edit user's/Reviewer's profile.
    """
    context = RequestContext(request)
    print request.user
    user = get_object_or_404(User, username=request.user)
    old_username = user.username
    print user.first_name
    print user.last_name
    reviewer = get_object_or_404(Reviewer, user=request.user)
    if request.method == 'POST':
        print "We've a request to register"
        reviewerform = ReviewerForm(data=request.POST, instance=reviewer)
        userform = UserForm(data=request.POST, instance=user)
        if reviewerform.is_valid() and userform.is_valid():
            print "Forms are Valid"
            user = userform.save(commit=False)
            if old_username != user.username:
                messages.error(request, 'Username cant be changed')
                context_dict = {'reviewerform': reviewerform,
                                'userform': userform}
                return render_to_response('reviewer_profile_edit.html',
                                          context_dict, context)
            user.set_password(user.password)
            user.save()
            reviewer = reviewerform.save(commit=False)
            if 'picture' in request.FILES:
                reviewer.picture = request.FILES['picture']
            reviewer.user = User.objects.get(username=user.username)
            reviewer.save()
            messages.success(request, "Profile updated successfully.")
        else:
            if reviewerform.errors or userform.errors:
                print reviewerform.errors, userform.errors
    else:
        reviewerform = ReviewerForm(instance=reviewer)
        userform = UserForm(instance=user)

    context_dict = {'reviewerform': reviewerform,
                    'userform': userform}
    return render_to_response('reviewer_profile_edit.html',
                              context_dict, context)


def content(request, lang):
    """
    Argument:

    `request`: This requests the particular content.

    `lang`: This indicates the language of the contents.
    """
    context = RequestContext(request)
    contributor = Contributor.objects.all()
    filter_review = Subject.objects.all().filter(review__gte=3)
    filter_lang = filter_review.filter(language__language=lang)
    uploads = filter_lang.order_by('class_number')
    count = len(uploads)
    context_dict = {
        'uploads': uploads,
        'contributor': contributor,
        'lang': lang,
	'count': count,
    }
    return render_to_response('content.html', context_dict, context)


def language_select(request):
    """
    Argument:

    `request`: This requests the particular content.
    """
    context = RequestContext(request)
    languages = Language.objects.values_list('language', flat=True)
    context_dict = {
        'languages': languages}
    return render_to_response('language_select.html', context_dict, context)


def search(request, lang):
    """
    Argument:

    `request`: This requests the searched content.

    `lang`: This indicates the language of the searched contents.
    """
    context = RequestContext(request)
    try:
        user = User.objects.get(username=request.user.username)
    except:
        user = None
    query = request.GET['q']
    filter_query = Subject.objects.filter(topic__icontains=query)
    filter_lang = filter_query.filter(language__language=lang)
    filter_review = filter_lang.filter(review__gte=3)
    results_topic = filter_review.order_by('class_number')
    filter_query = Subject.objects.filter(name__icontains=query)
    filter_lang = filter_query.filter(language__language=lang)
    filter_review = filter_lang.filter(review__gte=3)
    results_name = filter_review.order_by('class_number')
    template = loader.get_template('search.html')
    context = Context({'query': query,
                       'results_topic': results_topic,
                       'results_name': results_name,
                       'lang': lang,
                       'user': user})
    response = template.render(context)
    return HttpResponse(response)


def detail_user(request):
   """
   Argument:

   `request`: This function redirects to the page having detailed information of contributor and reviewer
   """
   context = RequestContext(request)
   contributor = Contributor.objects.all()
   reviewer = Reviewer.objects.all()
   if contributor:
       print contributor[0].picture
   else:
       print "Sorry, no contributor found."
   context_dict = {'contributor': contributor,
                   'reviewer': reviewer,
		  }
   return render_to_response('detail_user.html',context_dict,context)


def developer_team(request):
   """
   Argument:

   `request`: This function redirects to the page having detailed information of Developer team.
   """
   context = RequestContext(request)
   return render_to_response('developers_page.html',context)
