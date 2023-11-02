from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Booking,Course
import json

@csrf_exempt
def post_student(request):
    if request.method == 'POST':
        data=json.loads(request.body)
        booking=Booking(
            firstName=data['firstName'],
            lastName=data['lastName'],
            email=data['email'],
            phone=data['phone'],
            age=data['age'],
            coursesID_id=data['coursesID'],
                             
        )
        


        booking.save()
        return JsonResponse({'message': 'Booking successful!'}, status=201)
    else:
        return JsonResponse({'error': 'Invalid method'}, status=405)
    

def get_courses(request):
    courses=Course.objects.all()
    data = [{'id': course.id, 'name': course.coursesName, 'Description': course.Description,'img':course.image,'is_puplish':course.is_puplish,'cateoryID':course.cateoryID.categoryName } for course in courses]
    return JsonResponse(data,safe=False)


