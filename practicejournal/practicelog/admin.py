from django.contrib import admin
from .models import User, Exercise, Goal, PracticeGoal

# Register your models here.
admin.site.register(User)
admin.site.register(Exercise)
admin.site.register(Goal)
admin.site.register(PracticeGoal)
