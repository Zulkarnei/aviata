from asgiref.sync import sync_to_async
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

import uuid

from apps.airflow.models import Search
from apps.airflow.utils import parse, refresh_datas, check_curr_model
from apps.booking.models import Booking


# Create your views here.
class AirflowSearchView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        search = Search.objects.create()
        parse()
        return Response(dict(search_id=search.uuid))


@sync_to_async
@api_view(["GET"])
@permission_classes((AllowAny,))
def get_results(request, **kwargs):
    search_id = kwargs.get('search_id')
    currency = kwargs.get('currency')
    search_query = Search.objects.filter(uuid=search_id, currency=currency)
    if search_query.exists():
        search = search_query.first()
    else:
        Search.objects.filter(uuid=search_id).update(currency=currency, search_item=dict())
        search = Search.objects.get(uuid=search_id)

    check_curr_model(currency)

    if search.search_item:
        status = "COMPLETED"
    else:
        status = "PENDING"

    response_data = {
        "search_id": search_id,
        "status": status,
        "items": search.search_item,
    }

    refresh_datas(currency, search)

    return Response(response_data)
