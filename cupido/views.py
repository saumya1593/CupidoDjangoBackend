from rest_framework.views import APIView
import csv
import json
from django.http import HttpResponse
import io
from .services import Services


class CupidoView(APIView):

    def post(self,request):
        data = []
        file_path = request.FILES['CSV']

        conversion_keys_list = dict(request.data).get('conversion_keys_list')
        conversion_keys_int = dict(request.data).get('conversion_keys_int')
        conversion_keys_bool = dict(request.data).get('conversion_keys_bool')

        # Read CSV file to JSON
        for row in csv.DictReader(io.StringIO(file_path.read().decode('ISO-8859-1'))):
            data.append(row)
        file_path.seek(0)
        json_data = json.dumps(data)
        # Format the JSON data
        d = json.loads(json_data)

        parsed_data = Services.parse_data(d,conversion_keys_list,conversion_keys_int,conversion_keys_bool)

        return HttpResponse(json.dumps(parsed_data), content_type="application/json")

