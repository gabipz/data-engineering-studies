from pprint import pformat
from collections import Mapping


class JSONObject(Mapping):
    '''
    Class for transforming a simple Json file into a dict like object.
    Used for dealing with config files.
    '''

    def __init__(self, d):
        self.__dict__ = d

    def keys(self):
        return self.__dict__.keys()

    def __getitem__(self, key):
        return self.__dict__[key]

    def __iter__(self):
        return iter(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __repr__(self):
        ind = len(self)
        return pformat(self.__dict__, indent=ind)

    def to_dict(self):
        return self.__dict__


def ot(**kwargs):
    for k, v in kwargs.items():
        print(k, ':', v)
