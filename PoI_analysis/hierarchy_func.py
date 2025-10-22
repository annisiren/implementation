import statistics
import operator
from collections import Counter
from copy import deepcopy

class Course:
    def __init__(self, topic):
        self.tier = 'Course'
        # List of topic objects
        self.topic = topic
        self.value = self.list(self.topic)
        self.ccv = self.ccv(self.value)
        self.vcv = self.vcv(self.topic)

    def __add__(self, otherValue):
        return Course(self.value + otherValue.value)

    def list(self, t):
        value = t[0].value

        for v in t[1:]:
            value = self.combine_dicts(value, v.value)
        value['topic'] = 0
        value['lo'] = 0
        value['er'] = 0
        return value

    def combine_dicts(self, a, b, op=operator.add):
        return {k: a.get(k, 0) + b.get(k, 0) for k in a.keys() | b.keys()}

    def vcv_list(self, lo):
        value = {k: [d.value[k] for d in lo] for k in lo[0].value}
        value.pop('topic', None)
        value.pop('lo', None)
        value.pop('er', None)

        return value

    def ccv(self, v):
        v.pop('topic', None)
        v.pop('lo', None)
        v.pop('er', None)
        values = list(v.values())
        return round(statistics.stdev(values), 2) / round(statistics.mean(values), 2)

    def vcv(self, v):
        values = self.vcv_list(v)

        for key, value in values.items():
            values[key] = self.calculate_vcv(value)
        return values

    def calculate_vcv(self, v):
        try:
            return statistics.stdev(v)/statistics.mean(v)
        except:
            return 'N/A'

class Topic:
    def __init__(self, t, lo):
        self.tier = 'Topic'
        self.t = t

        # List of LO objects
        self.lo = lo

        self.value = self.list(self.lo)
        self.ccv = self.ccv(self.value)
        self.vcv = self.vcv(self.lo)

    def __add__(self, otherValue):
        return Topic(self.value + otherValue.value)

    def list(self, lo):
        value = lo[0].value
        for v in lo[1:]:
            value = self.combine_dicts(value, v.value)
        value['topic'] = self.t
        value['lo'] = 0
        value['er'] = 0

        return value

    def combine_dicts(self, a, b, op=operator.add):
        return {k: a.get(k, 0) + b.get(k, 0) for k in a.keys() | b.keys()}

    def vcv_list(self, lo):
        value = {k: [d.value[k] for d in lo] for k in lo[0].value}
        value.pop('topic', None)
        value.pop('lo', None)
        value.pop('er', None)

        return value

    def mean(self, v):
        return round(statistics.mean(v), 2)

    def stdev(self, v):
        return round(statistics.stdev(v), 2)

    def ccv(self, v):
        v.pop('topic', None)
        v.pop('lo', None)
        v.pop('er', None)
        values = list(v.values())
        return round(statistics.stdev(values), 2) / round(statistics.mean(values), 2)

    def vcv(self, v):
        values = self.vcv_list(v)

        for key, value in values.items():
            values[key] = self.calculate_vcv(value)
        return values

    def calculate_vcv(self, v):
        try:
            return statistics.stdev(v)/statistics.mean(v)
        except:
            return 'N/A'

class LearningObject:
    def __init__(self, t, lo, er):
        self.tier = 'LO'
        self.t = t
        self.lo = lo
        # List of ER objects
        self.er = er
        self.value = self.list(self.er)
        self.ccv = self.ccv(self.value)

    def __add__(self, otherValue):
        return LearningObject(self.value + otherValue.value)

    def list(self, er):
        value = er[0].value
        for v in er[1:]:
            value = self.combine_dicts(value, v.value)
        value['topic'] = self.t
        value['lo'] = self.lo
        value['er'] = 0
        return value

    def combine_dicts(self, a, b, op=operator.add):
        return {k: a.get(k, 0) + b.get(k, 0) for k in a.keys() | b.keys()}

    def mean(self, v):
        return round(statistics.mean(v), 2)

    def stdev(self, v):
        return round(statistics.stdev(v), 2)

    def ccv(self, v):
        v.pop('topic', None)
        v.pop('lo', None)
        v.pop('er', None)
        values = list(v.values())
        return round(statistics.stdev(values), 2) / round(statistics.mean(values), 2)

class EducationalResource:
    def __init__(self, t, lo, er, value):
        self.tier = 'ER'
        self.t = t
        self.lo = lo
        self.er = er

        self.value = self.to_int(value)

    def __add__(self, otherValue):
        return EducationalResource(self.value + otherValue.value)

    def to_int(self, value):
        return {k: int(v) if v.isdecimal() else v for k, v in value.items()}