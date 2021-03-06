"""I decided to write a code that generates data filtering object from a list of keyword parameters:"""


class Filter:
    """
    Helper filter class. Accepts a list of single-argument
    functions that return True if object in list conforms to some criteria
    """

    def __init__(self, *args):
        self.functions = list(args)

    def apply(self, data):
        print('self functions', self.functions)
        # for item in data:
        #     for test in self.functions:
        #         print(item, test(item))
        return [item for item in data if all(foo(item) for foo in self.functions)]


# example of usage:
# positive_even = Filter(
#     lambda a: a % 2 == 0, lambda a: a >= 0, lambda a: isinstance(a, int)
# )
# print(positive_even.apply(range(100)))  # should return only even numbers from 0 to 99


def make_filter(keywords):
    """
    Generate filter object for specified keywords
    """
    filter_funcs = []
    print('accepted kw', keywords)

    def new_filter(data):
        return

    for key, value in keywords.items():
        print(key, value)

        def keyword_filter_func(data):
            if key not in data:
                return False
            return key in data and data[key] == value
        # filter_funcs.append(lambda data: key in data and data[key] == value)
    return Filter(*filter_funcs)


sample_data = [
     {
         "name": "Bill",
         "last_name": "Gilbert",
         "occupation": "was here",
         "type": "person",
     },
     {
         "is_dead": True,
         "kind": "parrot",
         "type": "bird",
         "name": "polly"
     },
]

# should return only second entry from the list
# z = make_filter({'name': 'polly', 'type': 'bird'}).apply(sample_data)
# print(z)
"""There are multiple bugs in this code.
 Find them all and write tests for faulty cases."""
z = make_filter({'name': 'polly', 'job': 'janitor',  'last_name': "Gilbert", }).apply(sample_data)
print('fin rez', z)

# assert make_filter({'name': 'polly', 'type': 'bird'}).apply(sample_data) == [{
#          "is_dead": True,
#          "kind": "parrot",
#          "type": "bird",
#          "name": "polly"
#      }]
# assert make_filter({'name': 'polly', 'type': 'person'}).apply(sample_data) == []
