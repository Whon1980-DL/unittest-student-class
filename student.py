from datetime import date, timedelta
import requests


class Student:
    """ A Student class as base for method testing """
    
    # The underscore in front is to make it read only 
    # and to let other devloper know
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False

    # @property is added for a read only method
    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"
    
    @property
    def email(self):
        return f"{self._first_name.lower()}.{self._last_name.lower()}@email.com"
    
    def apply_extension(self, days):
        self.end_date = self.end_date + timedelta(days=days)

    def alert_santa(self):
        self.naughty_list = True

    def course_schedule(self):
        response = requests.get(f"http://company.com/course-schedule/{self._last_name}/{self._first_name}")

        if response.ok:
            return response.text
        else:
            return "Something went wrong with the request!"
    