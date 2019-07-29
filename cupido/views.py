from rest_framework.views import APIView
import csv
import json
import ast
from django.http import HttpResponse
import io

class CupidoView(APIView):

    def post(self,request):
        data = []
        file_path = request.FILES['CSV']

        # Read CSV file to JSON
        for row in csv.DictReader(io.StringIO(file_path.read().decode('utf-8'))):
            data.append(row)
        file_path.seek(0)
        json_data = json.dumps(data)

        # Format the JSON data
        d = json.loads(json_data)
        d[0]['filters'] = dict()
        for i in range(len(d)):
            for key, value in d[i].items():  # iter on both keys and values
                if key.startswith('filters.'):
                    k = key.split(".", 1)[1]
                    v = value
                    d[i]['filters'][k] = v

            delete = [key for key in d[0] if key.startswith('filters.')]
            for key in delete: del d[0][key]

            arr_data = ast.literal_eval(d[i].get('featuresAtGlance'))
            d[i]['featuresAtGlance'] = arr_data
            arr_data = ast.literal_eval(d[i].get('highlights'))
            d[i]['highlights'] = arr_data
            arr_data = ast.literal_eval(d[i].get('images'))
            d[i]['images'] = arr_data
            arr_data = ast.literal_eval(d[i].get('brand_image'))
            d[i]['brand_image'] = arr_data
            arr_data = ast.literal_eval(d[i].get('backdrop_image'))
            d[i]['backdrop_image'] = arr_data
            arr_data = ast.literal_eval(d[i].get('whyweloveit_image'))
            d[i]['whyweloveit_image'] = arr_data
            gender_data = d[i].get('gender')
            d[i]['gender'] = bool(gender_data)
            market_data = d[i].get('marketPrice')
            d[i]['marketPrice'] = int(market_data)

        return HttpResponse(json.dumps(d), content_type="application/json")