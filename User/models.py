from django.db import models

class Branch(models.Model):
    branch_name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    branch_slug = models.CharField(max_length=10, unique=True, null=False, blank=False)

    def __str__(self):
        return self.branch_name+'-'+self.branch_slug    

class User(models.Model):
    user_name = models.CharField(max_length=100, null=False, blank=False)
    user_email = models.CharField(max_length=100, unique=True, null=False, blank=False)
    user_password = models.CharField(max_length=20, null=False, blank=False)
    user_phone = models.CharField(max_length=20, null=True, blank=True)
    user_type = models.CharField(max_length=20, null=False, blank=False)
    user_branch = models.ForeignKey(to=Branch, on_delete=models.CASCADE)
    otp = models.IntegerField(null=True, blank=True)
    verifyStatus = models.BooleanField(default=False)

    def __str__(self):
        return self.user_name+'-'+self.user_type+'-'+self.user_branch.branch_name