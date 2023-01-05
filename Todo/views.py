import json
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from Todo.models import ToDoList

# Create your views here.

def index(request):
    return HttpResponse("Welcome to Home page")

@csrf_exempt
def create_todo(request):
    if request.method == 'POST':
        SLNo = request.POST.get('SLNo')
        Title = request.POST.get('Title')
        Desc = request.POST.get('Desc')
        
        todo = ToDoList.objects.filter(Title=Title) 
        todo = ToDoList.objects.filter(SLNo=SLNo) 

        print('.................................................', todo)
        if not todo:  
            todo_list = ToDoList(SLNo= SLNo,Title = Title, Desc = Desc)
            todo_list.save()
            data = {"status_code":201, 
                    "message" : 'Your Todo created successfully'}
            return HttpResponse(json.dumps(data), content_type = 'application/json')
        else:
            data = {"status_code":400, 
                    "message" : f'Employee with Title {Title} exists'}
            data = {"status_code":400, 
                    "message" : f'Employee with SLNo {SLNo} exists'}

            return HttpResponse(json.dumps(data), content_type = 'application/json')


@csrf_exempt
def update_todo(request):
    if request.method == 'POST':
        # Get the primary key of the ToDoList object to update
        SLNo = request.POST.get('SLNo')

        try:
            # Get the ToDoList object with the given primary key
            todo = ToDoList.objects.get(SLNo=SLNo)
            
            # Update the fields of the ToDoList object
            todo.Title = request.POST.get('Title')
            todo.Desc = request.POST.get('Desc')

            # Save the changes to the database
            todo.save()

            data = {"status_code": 200, "message": "ToDo updated successfully"}
            return HttpResponse(json.dumps(data), content_type='application/json')

        except ToDoList.DoesNotExist:
            data = {"status_code": 404, "message": "ToDo not found"}
            return HttpResponse(json.dumps(data), content_type='application/json')

@csrf_exempt
def delete_todo(request):
    if request.method == 'POST':
        # Get the primary key of the ToDoList object to delete
        SLNo = request.POST.get('SLNo')

        try:
            # Get the ToDoList object with the given primary key
            todo = ToDoList.objects.get(SLNo=SLNo)

            # Delete the ToDoList object
            todo.delete()


            data = {"status_code": 200, "message": "ToDo deleted successfully"}
            return HttpResponse(json.dumps(data), content_type='application/json')

        except ToDoList.DoesNotExist:
            data = {"status_code": 404, "message": "ToDo not found"}
            return HttpResponse(json.dumps(data), content_type='application/json')
