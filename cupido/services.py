import json
import ast
from .exceptions import KeyError

class Services():

    def parse_data(d,conversion_keys_list,conversion_keys_int,conversion_keys_bool):

        d[0]['filters'] = dict()

        for i in range(len(d)):
            for key, value in d[i].items():  # iter on both keys and values
                if key.startswith('filters.'):
                    k = key.split(".", 1)[1]
                    v = value
                    d[i]['filters'][k] = v

            delete = [key for key in d[0] if key.startswith('filters.')]
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
                        d[i][conversion_keys_bool[j]] = bool(bool_data)
                except KeyError:
                    print("Column not present in CSV")


            for j in range(len(conversion_keys_int)):
                print(conversion_keys_int[j])
                try:
                    if conversion_keys_int[j] not in list(d[i].keys()):
                        raise KeyError
                    else:
                        int_data = d[i].get(conversion_keys_int[j])
                        d[i][conversion_keys_int[j]] = int(int_data)
                except KeyError:
                    print("Column not present in CSV")

        return d

