from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import auth
from django.db import transaction
from django.contrib.auth.hashers import check_password




# Create your views here.

@csrf_exempt
@api_view(['POST'])
def register(request):
	try:
		email = request.data["email"].lower()
		password = request.data["password"]
		user_type = request.data["user_type"]
		gender = request.data["gender"]
	except KeyError as e:
		e = str(e)
		return Response({"success": "0", "message": f"Please provide {e}"}, status=400)
	except Exception as e:
		return Response({"success": "0", "message": "Something went wrong"}, status=400)
	try:
		with transaction.atomic():
			if User.objects.filter(email=email):
				return Response({"success": "0", "message": "Email already exists"}, status=400)
			else:
				user = User.objects.create_user(username=email, email=email, password=password, user_type=user_type)
				user.save()
				refresh = RefreshToken.for_user(user)
				refresh['user_id'] = user.id
				print(refresh)
				return Response({"success": "1", "message": "User registered successfully", "access": str(refresh.access_token), "refresh": str(refresh), "user": {"email": email, "gender": gender, "user_type": user_type}}, status=200)
	except Exception as e:
		print(e)
		return Response({"success": "0", "message": "Something went wrong"}, status=400)


@csrf_exempt
@api_view(['POST'])
def login(request):
	try:
		email = request.data["email"].lower()
		password = request.data["password"]
	except KeyError as e:
		e = str(e)
		return Response({"success": "0", "message": f"Please provide {e}"}, status=400)
	except Exception as e:
		return Response({"success": "0", "message": "Something went wrong"}, status=400)
	try:
		user = User.objects.filter(email=email).first()
		if user is None:
			return Response({"success": "0", "message": "Email doesnot exists"}, status=401)
		if not check_password(password, user.password):
			return Response({"success": "0", "message": "Incorrect Password"}, status=401)
		refresh = RefreshToken.for_user(user)
		refresh['user_id'] = user.id
		return Response({"success": "1", "message": "logged in successfully", "access": str(refresh.access_token), "refresh": str(refresh), "user": {"email": user.email, "user_type": user.user_type}}, status=200)
	except Exception as e:
		print(e)
		return Response({"success": "0", "message": "Something went wrong"}, status=400)


@csrf_exempt
@api_view(["POST"])
# @ValidateAuthenticationToken
def logout(request, user=None):
    return Response({"success": "1", "message": "Logged out successfully"})



