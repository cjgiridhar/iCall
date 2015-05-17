from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
# Create your models here.


guest_status_choices = (
    ('UNKNOWN', _('Unknown')),
    ('INVITED', _('Invitation Sent (only email known)')),
    ('IDENTIFIED', _('Identified (email and name known)')),
    ('VERIFIED', _('Verified e-mail address')),
    ('USER', _('Signed Up')),
)

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    is_verified = models.BooleanField(default=False)
    phone_number = models.CharField(max_length="50", blank=True, default='')
    title = models.CharField(max_length="50", blank=True, default='')
    company = models.CharField(max_length="50", blank=True, default='')
    status = models.CharField(max_length=10, choices=guest_status_choices, blank=False,
                              null=False, default='UNKNOWN')

    def __unicode__(self):
        return unicode(self.user)