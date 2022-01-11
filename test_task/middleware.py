from django.contrib.auth import get_user_model
from users.views import UserAcitvityView

User = get_user_model()


class SetLastRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        user = request.user
        if not user.is_anonymous and not isinstance(response.__dict__['renderer_context']['view'], UserAcitvityView):
            User.objects.set_last_request(user)

        return response
