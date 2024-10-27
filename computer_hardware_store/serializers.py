from rest_framework import serializers
from computer_hardware_store import models

class BuilderSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Builder
        fields = '__all__'

class ComputerSerializers(serializers.ModelSerializer):
    builder = BuilderSerializers(read_only=True)
    builder_id = serializers.IntegerField(required=False, allow_null=True)
    price = serializers.SerializerMethodField()

    class Meta:
        model = models.Computer
        fields = '__all__'

    def get_price(self, obj):
        if models.Storage.objects.filter(computer=obj).exists():
            return obj.storage.price
        return None