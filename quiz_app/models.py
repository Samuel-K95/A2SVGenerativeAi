from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    first_name = models.CharField(null=True, max_length=50)
    email = models.CharField(max_length=20)
    carrier = models.CharField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=5, null=True, blank=True)

    def __str__(self):
        return self.first_name


class Message(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    sent_date = models.DateTimeField(auto_now_add=True)
    is_received = models.BooleanField(default=True)

    def __str__(self):
        return f"Message from {self.user.username} - {self.sent_date}"


class Quiz(models.Model):
    size = models.IntegerField()
    generated_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    questions = models.TextField()
    user_score = models.IntegerField(default=0)

    def __str__(self):
        return f"Quiz {self.pk} - Generated by {self.generated_by.username}"


class GroupQuiz(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    completed = models.BooleanField(default=False)
    joined_members = models.ManyToManyField(CustomUser)

    def __str__(self):
        return f"Group Quiz {self.pk} - Quiz: {self.quiz} - Start Time: {self.start_time}"


class ScoreHolder(models.Model):
    group_quiz = models.ForeignKey(GroupQuiz, on_delete=models.CASCADE)
    competitor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"Score for Group Quiz {self.group_quiz.pk} - Competitor: {self.competitor.username} - Score: {self.score}"