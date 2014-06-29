User's guide
============

Introduction
------------

Aakash School Education is committed to offer the students free access
to its many academic resources. We seek to capitalize on the potential
of the internet to eliminate borders and geographic distance as
obstacles to the instantaneous exchange of knowledge and new
ideas. Unlike distance learning programs that charge tuition, provide
formal instruction and limit participation, we offer all course
materials free to everyone with online access. People from around the
world may upload their content and students can make use of our
extensive library of content from any computer with access to the
web. ASE does not require any registration and is not a
degree-granting or certificate-granting activity rather it is instead
an effort to share knowledge and make sure the students have access to
world class education content making full use of the Internet's
potential.

The main purpose of creating web Application is to initialize task,it
is an important part of the process. It requires putting together the
Web Application project goals and purpose.Defining Web Application,
Purpose, Goals and Direction establishes your project's clear
direction and helps you focus on setting and achieving your goal.


* Why Python-Django

  - Python is a very-high-level dynamic object-oriented programming
    language.It’s designed to be easy to learn, read and program.

  - *Python is open*: Python is open source software, distributed
      under a liberal license, and can thus be distributed freely.

  - *Python is general purpose*: Python is a general purpose language,
      which means that many things are made easy. Examples are string
      processing, reading/writing files, sockets, websites, databases,
      GUI’s.

  - *Python is dynamic*: Being a dynamic language means that new code
    can be executed during runtime without limitations.

  - Django is a high-level Python Web framework that encourages rapid
    development and clean, pragmatic design.

  - Django was designed to handle two challenges: the intensive
    deadlines of a newsroom and the stringent requirements of the
    experienced Web developers who wrote it.

  - Django's primary goal is to ease the creation of complex,
    database-driven websites. Django emphasizes reusability and
    "pluggability" of components, rapid development.

  - Django follows the model–view–controller architectural
    pattern.Lets dive into what is MVC Design Pattern.The first thing
    to note is that that we split it over four Python files
    (``models.py``, ``views.py``, ``urls.py``) and an HTML template
    (``latest_uploads.html``): 

  - ``models.py`` (the database tables) ::

	from django.db import models

	class Subject(models.Model):
	    name = models.CharField(max_length=50)
	    upload_date = models.DateField()


  - ``views.py`` (the business logic) ::

	from django.shortcuts import render
	from models import Subject

	def latest_uploads(request):
	    uploads_list = Subject.objects.order_by('-upload_date')[:10]
	    return render(request, 'latest_uploads.html', {'uploads_list': uploads_list})


  - ``urls.py`` (the URL configuration) ::

	from django.conf.urls.defaults import *
	import views

	urlpatterns = patterns('',
	    (r'^latest/$', views.latest_uploads),
	)


  - ``latest_uploads.html`` (the template) ::

	<html><head><title>Uploads</title></head>
	<body>
	<h1>Uploads</h1>
	<ul>
	{% for uploads in uploads_list %}
	<li>{{ uploads.name }}</li>
	{% endfor %}
	</ul>
	</body></html>  


Advantage of using python over other programming languages

- Python programs run slower than the Java codes, but python saves
  much time and space. Python programs are 3-5 times smaller than java
  programs.

- Python is dynamic typed language. Python programmers don't need to
  waste time in declaring variable types as in java. 

- The program length in python is 5-10 times shorter than that in C++.

- Unlike other programming languages python code has to be strictly
  indented but the indentation helps in much cleaner code(readable).

- High level data structures are list, directory are well suited in
  python.

- The elegant design and syntax rules of this programming language
  make it quite readable even among the multi programmer development
  teams.

**GIT**

- Git is a free and open source distributed version control system
  designed to handle everything from small to very large projects with
  speed and efficiency.

- Git allows groups of people to work on the same documents (often
  code) at the same time, and without stepping on each other's toes.

- GitHub is now the largest online storage space of collaborative
  works that exists in the world.

- If you and a co-worker are both updating code on the same
  website. You make your changes, save them, and upload them back to
  the website. So far, so good. The problem comes when your co-worker
  is working on the same code as you at the same time. One of you is
  about to have your work overwritten and erased.  A version control
  application like Git keeps that from happening.

- You and your co-worker can each upload your revisions to the same
  code, and Git will save two copies. Later, you can merge your
  changes together without losing any work along the way.

**GNU/Linux**

- GNU is a Unix-like computer operating system developed by the GNU
  Project. It is composed wholly of free software. It is based on the
  GNU Hurd kernel and is intended to be a "complete Unix-compatible
  software system".

- The system's basic components include the GNU Compiler Collection
  (GCC), the GNU C library (glibc), and GNU Core Utilities
  (coreutils), but also the GNU Debugger (GDB), GNU Binary Utilities
  (binutils),the bash shell and the GNOME desktop environment.

- The GNU Project has endorsed variants using the Linux kernel, such
  as gNewSense, Trisquel and Parabola GNU/Linux-libre.

- LINUX is also a Unix-like and mostly POSIX-compliant computer
  operating system assembled under the model of free and open source
  software development and distribution.

- The underlying source code may be used, modified, and
  distributed—commercially or non-commercially—by anyone under
  licenses such as the GNU General Public License.

- Typically, Linux is packaged in a format known as a Linux
  distribution for desktop and server use. Some popular mainstream
  Linux distributions include Debian, Ubuntu, Linux Mint, Fedora, Arch
  Linux, and the commercial Red Hat Enterprise Linux and SUSE Linux
  Enterprise Server.

- Linux distributions include the Linux kernel, supporting utilities
  and libraries and usually a large amount of application software to
  fulfill the distribution's intended use.

- The open-source software movement arose to clarify the environment
  that the new copyright, licensing, domain, and consumer issues
  created.

- Open-source code is typically a collaborative effort where
  programmers improve upon the source code and share the changes
  within the community so that other members can help improve it
  further.

- Distros designed to replace your existing operating system some
  other linux distros are Ubuntu,OpenSUSE,Fedora etc.

- Ubuntu is a Debian-based Linux operating system, with Unity as its
  default desktop environment (GNOME was the previous desktop
  environment).Ubuntu is the most popular desktop Linux distribution.

- The Ubuntu project is publicly committed to the principles of open
  source development; people are encouraged to use free software,
  study how it works, improve upon it, and distribute it.

Description
-----------

Workflow
~~~~~~~~

- A model is the single, definitive source of information about your
  data. It contains the essential fields and behaviors of the data
  you’re storing. Generally, each model maps to a single database
  table.Each attribute of the model represents a database field.

 *In this website the various models used :*

- User: This model stores the details of all the users, that is,
  contribuotrs and reviewers, of the website. The details include
  their username, first name, last name, password, email.

- Contributor: A contributor is an user of the website who can sign up
  by filling their user details, contact, picture and validation-docs
  in the registration form. The administrator will be notified about
  the new request from a user via a email and will verify the details
  of the contributor and if the access permissions are granted then
  he/she can upload study materials for the website.

- Reviewer: A reviewer is an user of the website who can sign up by
  filling their user details, contact and picture in the registration
  form. The administrator will be notified about the new request from
  a user via a email and will verify the details of the details of
  reviewer and if the access permissions are granted then they can
  review and give their comment on the unreviewed contents.

- Class: describes which class the study material belong to. Based on
  the class, the student accesses the study materials. Administrator
  stores number of classes in the database so that the contributor can
  contribute or the reviewer can review the content in a particular
  class.

- Subject: A contributor can upload content for the website by filling
  a form that includes subject name, topic, class-name and files that
  can be in pdf, video, animation formats. Rating can be given by
  administrator based on the capabilities of contributor upload.

- Comment: The comments are given by the reviewer on a topic of the
  subject. The date on which the comments are submitted are also noted
  along with the reviewer details.

   - Every user who logs in must be either a contributor or reviewer.
   - If the person who logs in, is a reviewer he/she can just see the
     materials but cannot modify the data. He can see the comments
     given by the reviewers but can not comment.
   - If the person who logs in, is a contributor he will be given
     permission to upload contents for the website. The contributor
     can see the comments given by the reviewers.
   - If the person who logs in, is a reviewer he will be given
     permission to review the uploaded content of the contributor and
     comment on it.
   - Reviewer doesn't have the permission to upload any files.
   - An upload will be available to the non-user if and only if it is
     approved by atleast 3 reviewers.
   - A non-user can search the study materials based on the subject
     name or topic.
   - A non-user may download the files which is pdf, video or
     animation files.

- Contact: Non-user can give their suggestions on the different
  contents or request for new contents. He/she can send their
  name,email id and message in order to contact the adminstrator.

- Faq: Faq consists of fields like questions and answers. It describes
  the frequently asked questions and answers by users.

- Language: Non-user can view the content in different languages
  mentioned in the model.


Interface
~~~~~~~~~

**User Interface**

User Interface for the "WebPortal" application begins with the
homepage of the portal, showing the recent uploads, number of
classes,subjects and uploads. It also have links to the Contact Us,
Content, Register(dropdown of contributor/reviewer), Login and more
pages which includes a dropdown of the Docs, About us and details of
the users.  Once a person is logged in, the login button changes to
his username and a dropdown comes on clicking his username, which
takes him to his profile or enables him to logout.



``Example:``


.. figure:: _static/img/homepage.png
   :height: 700 px
   :width: 1000 px
   :scale: 60 %
   :alt: Home Page
   :align: center

   Home page (before logging in)

.. figure:: _static/img/homepage1.png
   :height: 700 px
   :width: 1000 px
   :scale: 60 %
   :alt: Home Page
   :align: center

   Home page (after logging in)




**Contact Us**
  
  Clicking on this link redirects a user to a new page with a contact
  us form using which the user can contact the site administrators.


  ``Example:``

.. figure:: _static/img/contactus.png
   :height: 700 px
   :width: 1000 px
   :scale: 60 %
   :alt: Home Page
   :align: center

   Contact Us

**About us** Clicking on this link will give an overview of our
   website, regarding the main motive of this website and how will it
   help the students, and its relation to the Aakash School Education.

  ``Example:``

.. figure:: _static/img/aboutus.png
   :height: 700 px
   :width: 1000 px
   :scale: 60 %
   :alt: Home Page
   :align: center

   About Us


**Content**
  
  This section opens on clicking on the content link present in the
  homepage. This section is for showing the entire contents which is
  present in the website. Initially we have to Select a language in
  which we want to see the content.
  
   ``Example:``

.. figure:: _static/img/content.png
   :height: 700 px
   :width: 1000 px
   :scale: 60 %
   :alt: Home Page
   :align: center

   Select a language 

*Contents corresponding to that language*

  After selecting the language, the contents corresponding to that
  language will get displayed. It gets displayed in the form of a
  table with its fields as Class, Subject, Topic, Summary, PDF, Video
  and Animations present.

    ``Example:``

.. figure:: _static/img/content1.png
   :height: 700 px
   :width: 1000 px
   :scale: 60 %
   :alt: Home Page
   :align: center

   Contents corresponding to that language

*Search bar*

  There is also an option to search in the contents page. The search
  box provides us an option to enter either the subject or the topic
  of a subject, to search for. On clicking the search icon, the given
  string is matched with the available contents and wherever there is
  a match, the corresponding topics are displayed on the next
  page. Also there is a button to Go Back to the content's page.

    ``Example:``

.. figure:: _static/img/content2.png
   :height: 700 px
   :width: 1000 px
   :scale: 60 %
   :alt: Home Page
   :align: center

   Search

**Register**

  If a person wants to register in the website, he can do it
  here. There are 2 options for registering, i.e. As a Contributor or
  as a Reviewer.

*Register as a Contributor* This takes a user to register in the
  website as a Contributor i.e. the person who is going to upload the
  documents of various subjects and topics. He has to fill the form
  displayed in the page, the fields are username, firstname, lastname,
  email, password, profile picture, contact and the validation
  files(which checks if the contributor has the required qualification
  or not). Then he has to click the register button to get himself
  registered.

    ``Example:``

.. figure:: _static/img/regcon.png
   :height: 700 px
   :width: 1000 px
   :scale: 60 %
   :alt: Home Page
   :align: center

   Register as a contributor


*Register as a Reviewer* This takes a user to register in the website
  as a reviewer i.e. the person who is going to review the uploaded
  documents. He has to fill the form displayed in the page, the fields
  are username, firstname, lastname, email, password, profile picture
  and contact. Then he has to click the register button to get himself
  registered.

    ``Example:``

.. figure:: _static/img/regrev.png
   :height: 700 px
   :width: 1000 px
   :scale: 60 %
   :alt: Home Page
   :align: center

   Register as a reviewer

**Login** This is used by both the contributor and reviewer to
  Login. The user has to enter his username and password and the click
  on Sign In to login to his profile. In case his username and
  password do not match due to wrong credentials, he will get an error
  message saying Bad Login.

*Forgot Password* This is an option to let the user to retrieve his
  password in case he forgets it. He has to enter his email through
  which he registered in the website, and a mail will be sent which
  would contain his old password. He can then later login and change
  his password ( discussed later)

    ``Example:``

.. figure:: _static/img/login.png
   :height: 700 px
   :width: 1000 px
   :scale: 60 %
   :alt: Home Page
   :align: center

   Login

.. figure:: _static/img/forgot_pass.png
   :height: 600 px
   :width: 800 px
   :scale: 50 %
   :alt: Home Page
   :align: center

   Forgot Password

**Contributor's Profile** After a contributor logs in, it takes him to
  his profile, where he sees an "Upload more" button which when
  clicked takes him to the Upload Section. There are two more buttons
  i.e. Edit Profile and Change Password. These 3 buttons always remain
  fixed for the entire section when the contributor is logged in.  The
  first page he sees after logging in is the List of classes in which
  documents are uploaded.

The second page contains the list of subjects under a particular
class.

The third page contains the list of topics under a particular subject
and its details, such as Summary, PDF, Video and animation.

The fourth page contains the list of comments under a particular
topic.

    ``Example:``

.. figure:: _static/img/con.png
   :height: 1000 px
   :width: 1500 px
   :scale: 50 %
   :alt: Home Page
   :align: center
   
   Contributor Profile

*Upload More* When a contributor clicks on the upload more button, it
   takes him to the upload more form which contains various fields
   such as language, class, Subject name, topic, pdf, video, animation
   and summary. Once he fills the entire form, he clicks on upload
   more which uploads the content. If any required field is missing or
   it is not a valid file, it raises error. If none of PDF, video or
   animation is present, it raises an error. Also, there is a
   limitation of file size of pdf, upon exceeding it raises an error.

    ``Example:``

.. figure:: _static/img/upload.png
   :height: 700 px
   :width: 1000 px
   :scale: 60 %
   :alt: Home Page
   :align: center
   
   Upload more

**Reviewer's Profile** After a reviewer logs in, it takes him to his
   profile. Also he sees an "Past Approvals" button which when clicked
   takes him to his recent past approvals. There are two more buttons
   i.e. Edit Profile and Change Password. These 3 buttons always
   remain fixed for the entire time when the reviewer is logged in.
   The first page he sees after logging in is the list of classes in
   which documents are uploaded.

The second page contains the list of subjects under a particular
class.

The third page contains the list of topics under a particular subject
and its details, such as Summary, PDF, Video and animation.  Also,
there is an approve button which the reviewer has to click if he feels
that the uploaded documents are suitable for the topic and can be
published. If a topic is approved by 3 or more reviewers, it is deemed
accepted and published in the Content page.

The fourth page contains the list of comments under a particular
topic. Also, since the user is a reviewer, he has the freedom to add
any number of comments, and view all the previous comments on the
topic. Upon commenting, the date, time and username of the reviewer
comes beneath the comment. These comments are viewed by the the
contributor so that he can improve his uploaded content.


    ``Example:``

.. figure:: _static/img/rev.png
   :height: 1000 px
   :width: 1500 px
   :scale: 50 %
   :alt: Home Page
   :align: center
   
   Reviewer Profile

*Past Approvals* When a reviewer clicks on the "Past Approval" link,
   it takes him to the past approval table which contains various
   fields such as class, Subject name, topic, pdf, video, animation,
   summary and the Approved status. The content already approved by
   the reviewer previously in his profile will be displayed here.

.. figure:: _static/img/past.png
   :height: 800 px
   :width: 1200 px
   :scale: 60 %
   :alt: Home Page
   :align: center
   
   Past Approvals


* The next two sections are common both for contributor and reviewer

**Edit Profile** Upon clicking the edit profile button, the user
  (contributor or reviewer) can edit his profile. The user form and
  the contributor/reviewer form is displayed, with an instance of the
  contributor/reviewer present. So if a user wants to edit anything,
  he can see his previous information and feed in the new information
  i.e he can make new changes to his previous details. The password
  has to be filled again and then he has to click Save Changes to save
  the changes.

    ``Example:``

.. figure:: _static/img/editcon.png
   :height: 700 px
   :width: 1000 px
   :scale: 60 %
   :alt: Home Page
   :align: center
   
   Contributor Edit Profile

.. figure:: _static/img/editrev.png
   :height: 700 px
   :width: 1000 px
   :scale: 60 %
   :alt: Home Page
   :align: center
   
   Reviewer Edit Profile

**Change Password** Upon clicking this a new page opens up. The user
   has to enter his old password and his new password twice for
   confirmation.If the old password is correct and both the entered
   new passwords match, his password is changed and the success
   message is displayed, else an error message pops up.

.. figure:: _static/img/pass_change.png
   :height: 700 px
   :width: 1000 px
   :scale: 60 %
   :alt: Home Page
   :align: center
   
   Password Change


Conclusion
----------

- Students are given the opportunity to choose from various subjects
  and topics so that they can gain more knowledge. This is especially
  beneficial for those who live in rural areas that only have one or
  two educational facilities, which most of the time, offer limited
  course and program options for students.

- Another benefit of taking online tutorials, and probably the most
  popular one, would be that it offers flexibility to
  students. Because they can attend classes and courses whenever and
  wherever there is a computer and access to the internet, they can
  easily plan out a schedule that would work for them.

- Online learning allows a more student-centered teaching
  approach. Because every student has his or her way of learning that
  works for them, getting an online education may help in ensuring
  that each lesson or material is completely understood before moving
  on to the next, which in turn, could result to better learning.

- Online course materials can be accessed 24 hours a day every
  day. This means that students can easily read and review lectures,
  discussions and other materials relevant to their subjects. There
  are some students who find it a bit difficult to understand spoken
  material in a typical classroom setting because of a number of
  distractions, boredom or tiredness. Because they can simply access
  the material online once they are prepared to learn, students are
  able to take in and understand the material a lot better.

- Because of the flexibility offered by online learning, not only
  undergraduate students, but also individuals who already have
  full-time jobs or other commitments are able to take supplementary
  courses and even earn their college degrees online.

Reference
---------

- `<https://www.djangoproject.com/>`_

- `<http://www.tangowithdjango.com/>`_

- `<http://www.startbootstrap.com/>`_

- `<http://www.stackoverflow.com/>`_

- `<http://www.aakashlabs.org/>`_

- `<http://sphinx-doc.org>`_


