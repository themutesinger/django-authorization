from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as tr

from commons.constants import MENTOR, ADMIN, USER


class CustomUser(AbstractUser):

    USER_TYPE = (
        (MENTOR, 'Mentor'),
        (ADMIN, 'Admin'),
        (USER, 'User')
    )

    is_mentor = models.BooleanField(
        default=False,
        help_text=tr(
            'Поле для указания, является ли пользователь ментором'
        )
    )
    user_type = models.CharField(
        choices=USER_TYPE,
        default=USER,
        max_length=15
    )