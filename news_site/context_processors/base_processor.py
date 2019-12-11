from groups.models import Group
def index(request):
    groups = Group.objects.all()
    return {'groups':groups}