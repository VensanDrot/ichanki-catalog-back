import uuid


from apps.tools.models import ActionLog
from apps.tools.utils.signals import create_log


class ActionLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.uuid = uuid.uuid4()
        ActionLog.objects.create(uuid=request.uuid)
        response = self.get_response(request)
        self.log_action(request)
        return response

    def log_action(self, request):
        if hasattr(request, 'method') and request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            user = getattr(request, 'user', None)
            if user and user.is_authenticated:
                section = request.resolver_match.app_name.capitalize()
                action = self.get_action(request)
                create_log(request, action, user.username, section)

    @staticmethod
    def get_action(request):
        method = request.method
        if method == 'POST':
            return ActionLog.CREATE
        elif method == 'PUT' or method == 'PATCH':
            return ActionLog.EDIT
        elif method == 'DELETE':
            return ActionLog.DELETE
        # Add more conditions for other actions if needed
        return None
