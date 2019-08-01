import ast
from .exceptions import KeyError
from datetime import datetime

class Services():

    def parse_data(d,conversion_keys_list,conversion_keys_int,conversion_keys_bool):

        d[0]['filters'] = dict()
        d[0]['sale'] = dict()
        d[0]['sale']['cupidLove'] = dict()
        for i in range(len(d)):
            for key, value in d[i].items():  # iter on both keys and values
                if key.startswith('filters.'):
                    k = key.split(".", 1)[1]
                    if k=='Year':
                        v = Services.convert_year(value)
                    else:
                        v = value
                    d[i]['filters'][k] = v

            delete = [key for key in d[0] if key.startswith('filters.')]
            for key in delete: del d[0][key]

            for key, value in d[i].items():  # iter on both keys and values
                if key.startswith('sale.'):
                    k = key.split(".", 1)[1]
                    if k.startswith('cupidLove.'):
                        k_inner = k.split(".", 1)[1]
                        v_inner = Services.convert_to_int(value)
                        d[i]['sale']['cupidLove'][k_inner] = v_inner
                    else:
                        if k=='starttime' or k=='endtime':
                            v = Services.convert_date(value)
                        elif k=='salePrice':
                            v = Services.convert_to_int(value)
                        elif k=='referralPercent':
                            v = Services.convert_to_float(value)
                        else:
                            v = value
                        d[i]['sale'][k] = v

            delete = [key for key in d[0] if key.startswith('sale.')]
            for key in delete: del d[0][key]


            for j in range(len(conversion_keys_list)):

                try:
                    if conversion_keys_list[j] not in list(d[i].keys()):
                        print(conversion_keys_list[j])
                        raise KeyError
                    else:
                        arr_data = ast.literal_eval(d[i].get(conversion_keys_list[j]))
                        d[i][conversion_keys_list[j]] = arr_data
                except KeyError:
                    print("Column not present in CSV")


            for j in range(len(conversion_keys_bool)):
                try:
                    if conversion_keys_bool[j] not in list(d[i].keys()):
                        raise KeyError
                    else:
                        bool_data = d[i].get(conversion_keys_bool[j])
                        d[i][conversion_keys_bool[j]] = Services.convert_to_bool(bool_data)
                except KeyError:
                    print("Column not present in CSV")


            for j in range(len(conversion_keys_int)):
                print(conversion_keys_int[j])
                try:
                    if conversion_keys_int[j] not in list(d[i].keys()):
                        raise KeyError
                    else:
                        int_data = d[i].get(conversion_keys_int[j])
                        d[i][conversion_keys_int[j]] = Services.convert_to_int(int_data)
                except KeyError:
                    print("Column not present in CSV")

        return d

    @staticmethod
    def convert_year(str_data):
        datetime_object = datetime.strptime(str_data, '%Y')
        return datetime_object.year

    @staticmethod
    def convert_date(str_data):
        datetime_object = datetime.strptime(str_data, '%d/%m/%y').date()
        return datetime_object

    @staticmethod
    def convert_to_float(str_data):
        float_value = float(str_data)
        return float_value

    @staticmethod
    def convert_to_int(str_data):
        int_value = int(str_data)
        return int_value

    @staticmethod
    def convert_to_bool(str_data):
        bool_value = bool(str_data)
        return bool_value
