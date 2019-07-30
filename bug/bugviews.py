from django.shortcuts import render

# Create your views here.
from bug.models import Bug


#bug管理
def bug_manage(request):
    username = request.session.get('user', '')
    bug_list = Bug.objects.all()
    return render(request, "bug_manage.html", {"user": username,"bugs": bug_list})
