from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class EmailBackend:

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except ObjectDoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            user = User.objects.get(pk=user_id)
            return user
        except ObjectDoesNotExist:
            return None
