from django.db import models


class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    # goals = models.ManyToManyField()
    minutesPracticed = models.IntegerField()


class Exercise(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    comfortableTempo = models.IntegerField()


class Goal(models.Model):
    goalTypes = (("Short Term", "Short Term"), ("Long Term", "Long Term"))
    title = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=goalTypes, default="short")
    description = models.TextField(max_length=250)
    dateAdded = models.DateTimeField(auto_now_add=True)
    dateCompleted = models.DateTimeField(auto_now=True)


class PracticeGoal(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    dateAdded = models.DateTimeField(auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True)
