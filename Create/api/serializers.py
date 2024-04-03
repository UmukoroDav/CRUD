from rest_framework.serializers import ModelSerializer
from Create.models import Record



class RecordSerializers(ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'