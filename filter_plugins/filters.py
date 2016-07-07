import json

def max_int(input_data, maximum):
    if 0 < input_data < maximum:
        return input_data
    else:
        return maximum

def remove_element(input_data, hostname):
    input_data.remove(hostname)
    return json.dumps(input_data)

class FilterModule(object): 
    def filters(self): 
        return {'max_int': max_int, 'remove_element': remove_element}