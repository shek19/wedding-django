from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import generics,status
from rest_framework.exceptions import NotFound
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": serializer.data,
            "message": "User created successfully",
        }, status=status.HTTP_201_CREATED)

class WeddingViewSet(viewsets.ModelViewSet):
    queryset = Wedding.objects.all()
    serializer_class = WeddingSerializer

    def perform_create(self, serializer):
        serializer.save(planner = self.request.user)

class GuestViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        wedding_id = self.request.data.get('wedding')
        wedding = Wedding.objects.get(id=wedding_id)
        serializer.save(wedding=wedding)

class ChecklistViewSet(viewsets.ModelViewSet):
    queryset = Checklist.objects.all()
    serializer_class = ChecklistSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        wedding_id = self.request.data.get('wedding')
        wedding = Wedding.objects.get(id=wedding_id)
        serializer.save(wedding=wedding)

class BudgetItemViewSet(viewsets.ModelViewSet):
    queryset = BudgetItem.objects.all()
    serializer_class = BudgetItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        wedding_id = self.request.data.get('wedding')
        wedding = Wedding.objects.get(id=wedding_id)
        serializer.save(wedding=wedding)

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [IsAuthenticated]

class WeddingVendorViewSet(viewsets.ModelViewSet):
    queryset = WeddingVendor.objects.all()
    serializer_class = WeddingVendorSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        wedding_id = self.request.data.get('wedding')
        wedding = Wedding.objects.get(id=wedding_id)
        serializer.save(wedding=wedding)


class GuestDeleteView(generics.DestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    permission_class = [IsAuthenticated]


    #write the code for deleting the guest associated with the authenticated user
    def get_object(self):
        return super().get_object()

class GuestUpdateView(generics.UpdateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    permission_class = [IsAuthenticated]

    #write the code for deleting the guest associated with the authenticated user
    def get_object(self):
        return super().get_object()


class ChecklistDeleteView(generics.DestroyAPIView):
    serializer_class = ChecklistSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        weddings = Wedding.objects.filter(planner=self.request.user)
        return Checklist.objects.filter(wedding__in = weddings)

    def get_object(self):
        queryset = self.get_queryset()
        checklist_id = self.kwargs.get("pk")
        try:
            obj = queryset.get(pk=checklist_id)
            return obj
        except Checklist.DoesNotExist:
            raise NotFound("Checklist not found or does not belong to your weddings.")


class ChecklistUpdateView(generics.UpdateAPIView):
    serializer_class = ChecklistSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Get the weddings associated with the authenticated user
        weddings = Wedding.objects.filter(planner=self.request.user)
        # Return the checklists that are related to those weddings
        return Checklist.objects.filter(wedding__in=weddings)

    def get_object(self):
        queryset = self.get_queryset()
        checklist_id = self.kwargs.get("pk")  # Extract the checklist ID from the URL
        try:
            # Get the checklist object or raise 404 if not found
            obj = queryset.get(pk=checklist_id)
            return obj
        except Checklist.DoesNotExist:
            raise NotFound("Checklist not found or does not belong to your weddings.")