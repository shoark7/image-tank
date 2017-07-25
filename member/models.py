from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class MemberManager(BaseUserManager):
    def create_user(self, member_id, name, password, email=None):
        member_id = self.model.normalize_username(member_id)
        user = self.model(member_id=member_id,
                          name=name,
                          email=email,)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, member_id, name, password, email=None):
        user = self.create_user(member_id, name, password, email)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Member(AbstractBaseUser, PermissionsMixin):
    member_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=40, blank=True, null=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'member_id'
    REQUIRED_FIELDS = ['name',]

    objects = MemberManager()

    def __str__(self):
        return self.member_id

    def get_short_name(self):
        return self.__str__()

    def get_full_name(self):
        return self.member_id + ": " + self.name
