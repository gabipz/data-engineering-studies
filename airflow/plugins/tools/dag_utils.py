import json
import os
from json.decoder import JSONDecodeError

from airflow.models import Variable

from plugins.tools.json_to_object import JSONObject


def get_dag_config_object(dag_name):
    config_path = os.path.join(os.getcwd(),
                               'dags',
                               'configs',
                               f'{dag_name}.config.json')
    return get_config_object(config_path)


def get_config_object(config_path):
    with open(config_path, 'r') as config_file:
        config = json.load(config_file, object_hook=JSONObject)
    return config


def open_query(filepath):
    query_path = os.path.join(os.getcwd(), filepath)
    return open(query_path).read()


def create_dir_if_not_exists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


def get_airflow_variable(variable_name, json_encode=False):
    try:
        if json_encode:
            return json.loads(Variable.get(variable_name), object_hook=JSONObject)
        else:
            return Variable.get(variable_name)
    except JSONDecodeError as error:
        raise JSONDecodeError(f"ERROR - Can't decode variable \"{variable_name}\". Message: {error.msg}.",
                              error.doc,
                              error.pos)
    except TypeError as error:
        raise TypeError(f"ERROR - Invalid value found for variable \"{variable_name}\".")
    except KeyError:
        raise KeyError(f"ERROR - Unable to load variable \"{variable_name}\". Message: Variable not found.")
