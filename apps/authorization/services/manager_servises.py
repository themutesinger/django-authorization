

def create_user(
    user_model,
    *,
    last_name: str,
    first_name: str,
    password: str,
    email: str,
    **extra_field
):
    user = user_model(
        last_name=last_name,
        email=email,
        first_name=first_name,
        **extra_field
    )
    user.set_password(password=password)
    return user

