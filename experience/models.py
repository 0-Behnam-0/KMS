from django.db import models

# Create your models here.

# file = models.FileField(null=True, blank=True, upload_to ='uploads/%Y/%m/%d/', validators=[FileExtensionValidator( ['pdf', 'txt'] ) ])


class User(models.Model):
    first_name = models.CharField("First name", max_length=126)
    last_name = models.CharField("Last name", max_length=126)
    username = models.CharField(max_length=126, unique=True)
    national_code = models.IntegerField(unique=True)
    evidence = models.TextField()
    phone = models.IntegerField(unique=True)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.username
    


class Tree(models.Model):
    title = models.CharField(max_length=126)
    code = models.CharField(max_length=126, unique=True)
    root_code = models.CharField(max_length=126)


class Main(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE)
    title = models.CharField(max_length=126)
    publish_date = models.DateTimeField("Publish date", auto_now=True)
    description = models.TextField(blank=True)


class Tag(models.Model):
    title = models.CharField(max_length=126)
    description = models.TextField(blank=True)
    publish_date = models.DateTimeField("Publish date", blank=True, auto_now=True)


class TagLink(models.Model):
    main = models.ForeignKey(Main, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class Position(models.Model):
    title = models.CharField(max_length=126)
    appointment_date = models.DateTimeField("Appointment date")
    dismissal_date = models.DateTimeField("Dismissal date")


class PositionLink(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)


class Repository(models.Model):
    name = models.CharField(max_length=126)
    type = models.CharField(max_length=126)
    url = models.URLField(unique=True)
    description = models.TextField(blank=True)


class MediaLink(models.Model):
    main = models.ForeignKey(Main, on_delete=models.CASCADE)
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    start_time = models.TimeField("Start time", default=(0,0,0))
    end_time = models.TimeField("End time", default=(0,0,0))
    description = models.TextField(blank=True)


class DocumentLink(models.Model):
    main = models.ForeignKey(Main, on_delete=models.CASCADE)
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    related_part = models.TextField()
    description = models.TextField(blank=True)
