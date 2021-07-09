from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import EmailField


class CustomEmailValidationOnForgotPassword(PasswordResetForm):
    email = EmailField(max_length=254)

    error_messages = {
        'unknown': ("That email address doesn't have an associated "
                    "user account. Are you sure you've registered?"),
        'unusable': ("The user account associated with this email "
                     "address cannot reset the password."),
    }

    def clean_email(self):
        """
        Validates that an active user exists with the given email address.
        """
        email = self.cleaned_data["email"]
        self.users_cache = get_user_model()._default_manager.filter(email__iexact=email)
        if not len(self.users_cache):
            raise ValidationError(self.error_messages['unknown'])
        if not any(user.is_active for user in self.users_cache):
            # none of the filtered users are active
            raise ValidationError(self.error_messages['unknown'])
        if any((user.password == user.set_unusable_password())
               for user in self.users_cache):
            raise ValidationError(self.error_messages['unusable'])
        return email


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)
