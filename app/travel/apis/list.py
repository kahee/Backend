
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from travel.models import TravelInformation
from travel.serializer import TravelInformationSerializer

class TravelInformationView(APIView):
    def get(self, request, **kwargs):
        travel_informations = TravelInformation.objects.filter(city__name=kwargs['cityname'])
        serializer = TravelInformationSerializer(travel_informations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
