import datetime

import requests
from django.utils import timezone

from apps.airflow.models import Currency
from apps.booking.models import Booking, Flight, Segment, Price
import json

from apps.booking.utils import extract_data


def parse():
    data_1 = extract_data(r'./response_a.json')
    data_2 = extract_data(r'./response_b.json')
    data = data_1 + data_2
    for booking in data:
        flights = booking.get('flights')
        booking_instance, _ = Booking.objects.get_or_create(
            refundable=booking['refundable'],
            validating_airline=booking['validating_airline'],
        )
        Price.objects.get_or_create(
            booking=booking_instance,
            defaults=dict(
                total=booking['pricing']['total'],
                base=booking['pricing']['base'],
                taxes=booking['pricing']['taxes'],
                currency=booking['pricing']['currency']
            ),
        )
        for flight in flights:
            segments = flight.get('segments')
            flight_instance, _ = Flight.objects.get_or_create(
                booking=booking_instance,
                duration=flight['duration'],
            )
            for segment in segments:
                segment_instance, _ = Segment.objects.get_or_create(
                    operating_airline=segment['operating_airline'],
                    marketing_airline=segment['marketing_airline'],
                    flight_number=segment['flight_number'],
                    equipment=segment['equipment'],
                    dep=segment['dep'],
                    arr=segment['arr'],
                    baggage=segment['baggage']
                )
    return


def refresh_datas(currency, search):
    booking_query = Booking.objects.order_by('price__total')
    res_list = []
    current_curr = Currency.objects.get(title=currency)

    for booking in booking_query:
        if currency == booking.price.currency:
            amount = booking.price.total
        elif booking.price.currency == "KZT":
            amount = booking.price.total * current_curr.description
        else:
            desc = Currency.objects.get(title=booking.price.currency).description
            amount = desc * booking.price.total
        data = {
            'price': {"amount": round(amount, 2), "currency": currency},
            "pricing": {
                    'total': booking.price.total,
                    'base': booking.price.base,
                    'taxes': booking.price.taxes,
                    'currency': booking.price.currency
            }
        }
        res_list.append(data)

    search.search_item = res_list
    search.save(update_fields=['search_item'])
    return


def conversion_currency(currency):
    import xmltodict
    str_date = datetime.datetime.strftime(timezone.localtime().date(), "%d.%m.%Y")
    url = f"https://www.nationalbank.kz/rss/get_rates.cfm?fdate={str_date}"
    res = requests.get(url)

    data = xmltodict.parse(res.content).get('rates')['item']
    for curr in data:
        Currency.objects.get_or_create(
            fullname=curr['fullname'],
            defaults=dict(
                title=curr['title'],
                description=curr['description']
            )
        )
    Currency.objects.get_or_create(
        fullname=['Казахстанский тенге'],
        defaults=dict(
            title="KZT",
            description=1
        )
    )
    return res


def check_curr_model(currency):
    if not Currency.objects.filter(title=currency).exists():
        conversion_currency(currency)
    return True