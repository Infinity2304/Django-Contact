from rest_framework.response import Response
from rest_framework import status
from .serializer import UserSerializer, ContactSerializer
from rest_framework.decorators import api_view
from .models import User, Contact
from django.db.utils import IntegrityError
from django.shortcuts import get_object_or_404

# Create your views here.



#For AUTH page
@api_view(['POST'])
def signUp(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Please provide username and password.'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)

    user = User(username= username)
    user.set_password(password)
    user.save()
    response = Response({'message': 'User signed up'}, status=status.HTTP_201_CREATED) 
    response.set_cookie('user_id', user.id, httponly=True, secure=True, samesite='Strict')
    return response

@api_view(['POST'])
def login(request):
    username = request.data.get('username') 
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Please provide username and password.'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        user = User.objects.get(username=username)
        if user.check_password(password):
            serializedData = UserSerializer(user)
            response = Response(serializedData.data, status=status.HTTP_200_OK) 
            response.set_cookie('user_id', user.id, httponly=True, secure=True, samesite='None', path='/')
            return response
        else:
            return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
    except User.DoesNotExist:
        return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def logout(request):
    response = Response({'message': 'Logout successful.'}, status=status.HTTP_200_OK)
    response.delete_cookie('user_id')
    return response


#For CONTACT page
@api_view(['POST'])
def saveContact(request):
    try:
        data = request.data
        user_id = request.COOKIES.get('user_id')
        user = get_object_or_404(User, id=user_id)

        #Unique fields check
        number = data.get('number')
        email = data.get('email')
        if Contact.objects.filter(user=user, number=number).exists():
            return Response({'error': 'This number already exists'}, status=status.HTTP_400_BAD_REQUEST)
        if Contact.objects.filter(user=user, email=email).exists():
            return Response({'error': 'This email already exists'}, status=status.HTTP_400_BAD_REQUEST)

        data['user'] = user.id

        serializedData = ContactSerializer(data=data)
        if serializedData.is_valid():
            serializedData.save()
            return Response({'message': 'Contact Saved'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializedData.errors, status=status.HTTP_400_BAD_REQUEST)
    except IntegrityError:
        return Response({'error':'Internal Server Error'}, status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return Response({'error': 'User not logged in or not found'}, status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(['GET'])
def getContact(request):
    
    name = request.query_params.get('name')
    number = request.query_params.get('number')
    city = request.query_params.get('city')
    comment = request.query_params.get('comment')

    user_id = request.COOKIES.get('user_id')
    user = get_object_or_404(User, id=user_id)

    if not name and not number and not city and not comment:
        return Response({'error':'Please Enter the data'}, status=status.HTTP_400_BAD_REQUEST)
    
    filters = {'user': user}

    if name:
        filters['name__icontains'] = name
    elif number:
        filters['number__icontains'] = number
    elif city:
        filters['city__icontains'] = city
    elif comment:
        filters['comment__icontains'] = comment

    contact = Contact.objects.filter(**filters)
    serialized_contact = ContactSerializer(contact, many=True)
    if not contact:
        return Response({'error':'No contact found with this name'}, status=status.HTTP_404_NOT_FOUND)
    return Response(serialized_contact.data,status=status.HTTP_200_OK)


@api_view(['PUT'])
def updateContact(request, pk):
    try:
        contact = get_object_or_404(Contact, pk=pk, user_id=request.COOKIES.get('user_id'))
    except Contact.DoesNotExist:
        return Response({'error': 'Contact not found or does not belong to the user'}, status=status.HTTP_404_NOT_FOUND)
    
    serializedContact = ContactSerializer(contact, data=request.data, partial=True)
    if serializedContact.is_valid():
        serializedContact.save()
        return Response({'message':'Contact Updated'}, status=status.HTTP_200_OK)   
    else:
        return Response(serializedContact.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteContact(request, pk):
    try:
        contact = get_object_or_404(Contact, pk=pk, user_id=request.COOKIES.get('user_id'))
    except Contact.DoesNotExist:
        return Response({'error': 'Contact not found'}, status=status.HTTP_404_NOT_FOUND)
    
    contact.delete()
    return Response({'message':'Contact Deleted'}, status=status.HTTP_200_OK)


#######
@api_view(['GET'])
def getAll(request):
    contact = Contact.objects.all()
    serializedContact = ContactSerializer(contact, many= True)

    return Response(serializedContact.data)