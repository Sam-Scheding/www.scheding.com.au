import pickle
from rest_framework import serializers
from api.account_details.models import UserDetails, Link


class UserDetailsSerializer(serializers.ModelSerializer):

    # class OnlinePresenceField(serializers.CharField):
    #
    #     def to_representation(self, links):
    #         links = links.all()
    #         return "".join([("{}: {}\n".format(link.name, link.url)) for link in links]).rstrip()
    #
    # online_presence = OnlinePresenceField()

    class Meta:
        model = UserDetails
        # fields = '__all__'
        exclude = ('online_presence',)

class LinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Link
        fields = '__all__'
