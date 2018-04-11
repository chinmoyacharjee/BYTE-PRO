from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from datetime import datetime

def user_directory_path(instance, filename):
    return '{0}/{1}'.format(instance.user.username, filename)

class UserInformation(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    name = models.CharField(default="None", max_length=200)
    biography = models.TextField(default="None",)
    profilePicture = models.FileField(default='../media/defaultProfilePic.png',upload_to=user_directory_path,)

    def __str__(self):
        return self.name

class SkillTag(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    # user = models.OneToOneField(
    #     User,
    #     on_delete=models.CASCADE,
    #     primary_key=True
    # )
    skilltag=models.CharField(default='NONE',max_length=20,blank=True)




class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    projectName=models.CharField(max_length=250,blank=False)
    projectDescription = models.TextField(blank=False)
    accessType = models.CharField(default="Public" , max_length=25)
    projectCreatedAt = models.DateTimeField(default=datetime.now, blank=True)


class ProjectTag(models.Model):
    project=models.ForeignKey(Project, on_delete=models.CASCADE)
    projecttag=models.CharField(default='NONE',max_length=20)