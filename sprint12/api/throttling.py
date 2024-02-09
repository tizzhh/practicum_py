import datetime as dt

from rest_framework import throttling


class LunchBreakThrottle(throttling.BaseThrottle):
    def allow_request(self, request, view):
        cur_hour = dt.datetime.now().hour
        if 13 <= cur_hour <= 14:
            return False
        return True
