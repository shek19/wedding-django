from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BudgetItemViewSet, ChecklistDeleteView, ChecklistUpdateView, GuestDeleteView, GuestUpdateView, GuestViewSet, RegisterView, VendorViewSet, WeddingVendorViewSet, WeddingViewSet,ChecklistViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'wedding', WeddingViewSet)
router.register(r'guest', GuestViewSet)
router.register(r'checklist',ChecklistViewSet)
router.register(r'budgetitem', BudgetItemViewSet)
router.register(r'vendor',VendorViewSet)
router.register(r'weddingvendor',WeddingVendorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('guest/<int:pk>/delete/',GuestDeleteView.as_view(),name='guest-delete'),
    path('guest/<int:pk>/update/',GuestUpdateView.as_view(), name = "guest-update" ),
    path('checklist/<int:pk>/update/',ChecklistUpdateView.as_view(), name= "checklist-update"),
    path('checklist/<int:pk>/delete/',ChecklistDeleteView.as_view(), name = "checklist-update"),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Use TokenObtainPairView for login
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',RegisterView.as_view(), name= 'register')
]