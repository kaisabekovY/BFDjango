from django.shortcuts import render

def index(request):
    return render(request,'todos/1/completed/completed_todo_list.html')
def mainlist(request):
    return render(request,'todos/todo_list.html')
# Create your views here.
