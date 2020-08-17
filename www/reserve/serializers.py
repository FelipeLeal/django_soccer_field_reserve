from rest_framework import serializers

from reserve.models import Reserve


class ReserveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reserve
        fields = ['day', 'block', 'reserve_price']