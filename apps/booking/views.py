from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.booking.utils import extract_data
from time import sleep


class ProviderAView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        response_a = extract_data(r'./response_a.json')
        sleep(30)
        return Response(response_a)


class ProviderBView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        response_b = extract_data(r'./response_b.json')
        sleep(60)
        return Response(response_b)
