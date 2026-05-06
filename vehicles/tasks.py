from celery import shared_task
from vehicles.models import Vehicle
import requests
from bs4 import BeautifulSoup


@shared_task
def complete_vehicle_data(license_plate):
    url = 'https://pycodebr.com.br/placas-carros/'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    rows = soup.select('table tr')

    brand = model = color = None

    for row in rows:
        cols = [c.text.strip() for c in row.find_all('td')]
        if cols and cols[0] == license_plate:
            brand, model, color = cols[1], cols[2], cols[3]
            break

    if brand:
        Vehicle.objects.filter(
            license_plate=license_plate
        ).update(
            brand=brand,
            model=model,
            color=color,
        )