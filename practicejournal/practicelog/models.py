from django.db import models


class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    # goals =
    # practiceGoals =
    minutesPracticed = models.IntegerField()

    def __str__(self):
        return self.firstName


class Exercise(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    comfortableTempo = models.IntegerField()

    def __str__(self):
        return self.title


class Goal(models.Model):
    goalTypes = (("Short Term", "Short Term"), ("Long Term", "Long Term"))
    title = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=goalTypes, default="short")
    description = models.TextField(max_length=250)
    dateAdded = models.DateTimeField(auto_now_add=True)
    dateCompleted = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class PracticeGoal(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    dateAdded = models.DateTimeField(auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
