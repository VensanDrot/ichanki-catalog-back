# from apps.tools.models import ActionLog
from django.utils import timezone
from apps.tools.models import ActionLog


def update_log(request, instance):
    log_activity = ActionLog.objects.get(uuid=request.uuid)
    log_activity.item = f'{instance.id}'
    log_activity.save()


def create_log(request, action, username, section):
    ActionLog.objects.filter(uuid=request.uuid).update(
        created_at=timezone.now(),
        action=action,
        username=username,
        section=section
    )
