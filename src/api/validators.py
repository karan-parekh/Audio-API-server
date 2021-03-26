from datetime import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def datetime_validator(d):
    now   = timezone.now()
    today = datetime(now.year, now.month, now.day)
    date  = datetime(d.year, d.month, d.day)
    if date < today:
        raise ValidationError(_("Date cannot be in the past"))


def duration_validator(d):
    if d < 0:
        raise ValidationError(_("Duration cannot be negative")) 
