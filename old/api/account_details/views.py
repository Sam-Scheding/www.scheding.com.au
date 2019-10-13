from api.account_details.models import UserDetails, Link
from api.account_details.serializers import UserDetailsSerializer, LinkSerializer
from rest_framework import viewsets

# /api/accounts/details
class UserDetailsView(viewsets.ModelViewSet):

    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsSerializer


# /api/accounts/links
class LinkView(viewsets.ModelViewSet):

    queryset = Link.objects.all()
    serializer_class = LinkSerializer
