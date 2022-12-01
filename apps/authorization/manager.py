from django.contrib.auth.base_user import BaseUserManager

from authorization.services.validating import validate_email
from authorization.services.manager_servises import create_user


class CustomUserManager(BaseUserManager):

    def create_user(
        self,
        *,
        last_name: str,
        first_name: str,
        password: str,
        email: str,
        **extra_field
    ):
        email_exists = validate_email(email=email)
        if not email_exists:
            raise ValueError('Пустой эмайл')
        email = self.normalize_email(email=email)
        user = create_user(
            last_name=last_name,
            first_name=first_name,
            email=email,
            password=password,
            **extra_field
        )
        user.save(using=self._db)
        return user

