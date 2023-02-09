# RSS_feedreader_in_CommandPrompt
Developed RSS to give continous update of your favourite websites whenever a post s updated throught the windows commandline using django<this majorly focuses on windows users.for linux distros guys,am sory her though am a nerd>

## To make this more  paractical
I created first my blog using django and  then gave it its own rss feed 
that would be to provide update on any new update

 **steps:**
 1:Create django project(django-admin startproject projectname)<br />
 2:Then create project(python manage.py startapp appname )<br />

 you will be good to go,,,the project majorly involes the following file to work on:<br />
        -.settings.py-for your app registration<br />
        -.models.py-for your blog registration<br />
        -.urls.py-for your blog pagination<br />
        -.views.py-for your your blog context,,,how you want the blog to appear<br />
        -.feeds.py(or whichever name you give to your scripts)-for your blog feeds pick<br />

