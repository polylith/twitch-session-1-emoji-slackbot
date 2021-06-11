from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from employee.models import Employee


@api_view(['POST'])
def set_employee_emoji(request: Request) -> Response:
    print(request.data)

    Employee.objects.update_or_create(
        slack_user_id=request.data.get("user"),
        defaults={
            "last_emoji": request.data.get("smiley")
        }
    )

    return Response(data={})