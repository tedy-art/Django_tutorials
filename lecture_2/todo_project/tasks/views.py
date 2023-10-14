from django.shortcuts import render
from datetime import datetime

current_tasks =[
    "Create a simple django project.",
    "learn about template function django provide.",
    "Learn how to deploy a project.",
]
# Create your views here.
def index(request):
    return render(request, 'index.html',
                  context={
                      'cur_date' : str(datetime.now()),
                      'tasks' : current_tasks,
                  }
    )