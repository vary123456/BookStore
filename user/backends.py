from django.contrib.auth.models import User

class EmailBackend:
    def authenticate(self, request, **credentials):
        email = credentials.get('email')
        try:
            user = User.objects.get(email=email)
        except Exception as e:
            print(e)
        else:
            if user.check_password(credentials.get('password')):
                return user
