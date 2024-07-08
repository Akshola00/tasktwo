# api/views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from myauth.models import User
from .models import Organisation
from .serializers import UserSerializer, OrganizationSerializer, OrganizationCreateSerializer
from rest_framework.exceptions import PermissionDenied



class CreateOrganizationView(generics.CreateAPIView):
    serializer_class = OrganizationCreateSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        organization = serializer.save()

        response_data = {
            "status": "success",
            "message": "Organization created successfully",
            "data": {
                "orgId": organization.org_id,
                "name": organization.name,
                "description": organization.description
            }
        }

        return Response(response_data, status=status.HTTP_201_CREATED)

class OrganizationDetailView(generics.RetrieveAPIView):
    queryset = Organisation.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'org_id'

    def get(self, request, *args, **kwargs):
        organization = self.get_object()

        # Check if the user is part of the organization
        if request.user not in organization.users.all():
            raise PermissionDenied("You do not have permission to access this organization.")

        serializer = self.get_serializer(organization)
        response_data = {
            "status": "success",
            "message": "Organization retrieved successfully",
            "data": serializer.data
        }

        return Response(response_data, status=status.HTTP_200_OK)

class ListUserOrganizationsView(generics.ListAPIView):
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Organisation.objects.filter(users=user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        response_data = {
            "status": "success",
            "message": "Organizations retrieved successfully",
            "data": {
                "organisations": serializer.data
            }
        }

        return Response(response_data, status=status.HTTP_200_OK)

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_id = self.kwargs['pk']
        print(f"User ID received: {user_id}")  # Debugging line
        try:
            # Fetch the user based on string ID
            user = User.objects.get(userId=user_id)
            if request.user == user or request.user.organisations.filter(id=user_id).exists():
                serializer = self.get_serializer(user)
                return Response({
                    "status": "success",
                    "message": "User retrieved successfully",
                    "data": serializer.data
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "status": "error",
                    "message": "You do not have permission to view this user",
                    "statusCode": 403
                }, status=status.HTTP_403_FORBIDDEN)
        except User.DoesNotExist:
            return Response({
                "status": "error",
                "message": "User not found",
                "statusCode": 404
            }, status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response({
                "status": "error",
                "message": "Invalid user ID format",
                "statusCode": 400
            }, status=status.HTTP_400_BAD_REQUEST)
# class UserDetailView(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated]
#     lookup_field = 'pk'

#     def get(self, request, *args, **kwargs):
#         user_id = self.kwargs['pk']
#         user = self.get_object()
#         if request.user == user or request.user.organisations.filter(id=user_id).exists():
#             serializer = self.get_serializer(user)
#             return Response({
#                 "status": "success",
#                 "message": "User retrieved successfully",
#                 "data": serializer.data
#             }, status=status.HTTP_200_OK)
#         else:
#             return Response({
#                 "status": "error",
#                 "message": "You do not have permission to view this user",
#                 "statusCode": 403
#             }, status=status.HTTP_403_FORBIDDEN)
   
 