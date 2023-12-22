from email._header_value_parser import ContentType

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
import datetime
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from django.utils.text import slugify
from django.db.models.signals import post_save
from django.urls import reverse


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)
    address = models.CharField(max_length=100)
    image = models.ImageField(_("Image"), upload_to='Profile_img', blank=True, null=True)
    join_date = models.DateTimeField(_("join date"), default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user)
        super(Profile, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return '%s' % (self.user)

    def get_absolute_url(self):
        if self.slug:
            return reverse('accounts:profile_edit', kwargs={'slug': self.slug})
        return ''

    @receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        else:
            instance.profile.save()


def create_user_permission():
    # الحصول على نموذج المستخدم (User) من ContentType
    user_content_type = ContentType.objects.get_for_model(User)
    # إنشاء التصريح للمستخدمين العاديين لتمكينهم من تسجيل الدخول
    user_permission = Permission.objects.create(
        codename='can_login',
        name='Can Login',
        content_type=user_content_type,
    )
