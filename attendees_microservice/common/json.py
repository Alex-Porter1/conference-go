from json import JSONEncoder
from datetime import datetime
from django.db.models import QuerySet

class DateEncoder(JSONEncoder):
    def default(self, o):
        # if o is an instance of datetime
        if isinstance(o, datetime):
            return o.isoformat()
        #    return o.isoformat()
        else:
            return super().default(o)
        # otherwise
        #    return super().default(o)

class QuerySetEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, QuerySet):
            return list(o)
        else:
            return super().default(o)

class ModelEncoder(DateEncoder, QuerySetEncoder, JSONEncoder):
    encoders = {}


    def default(self, o):
        if isinstance(o, self.model):
            d = {}
            # if o has the attribute get_api_url
            if hasattr(o, "get_api_url"):
            #    then add its return value to the dictionary
                d["href"] = o.get_api_url()
            #    with the key "href"
            for property in self.properties:
        #     * for each name in the properties list
                value = getattr(o, property)
                if property in self.encoders:
                    encoder = self.encoders[property]
                    value = encoder.default(value)
                d[property] = value
        #         * put it into the dictionary with that property name as
        #           the key
        #     * return the dictionary
            d.update(self.get_extra_data(o))
            return d
        #   otherwise,
        #       return super().default(o)  # From the documentation
        else:
            return super().default(o)

    
    def get_extra_data(self, o):
        return {}

