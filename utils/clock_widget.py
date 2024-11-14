# utils/clock_widget.py
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.clock import Clock as KivyClock
from math import cos, sin, radians
from datetime import datetime

class ClockWidget(Widget):
    radius = NumericProperty(100)
    hour_hand_x = NumericProperty(0)
    hour_hand_y = NumericProperty(0)
    minute_hand_x = NumericProperty(0)
    minute_hand_y = NumericProperty(0)
    second_hand_x = NumericProperty(0)
    second_hand_y = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        KivyClock.schedule_interval(self.update, 1)

    def update(self, dt):
        now = datetime.now()
        self.update_hands(now.hour, now.minute, now.second)

    def update_hands(self, hour, minute, second):
        hour_angle = 360 * (hour % 12) / 12 - 90
        minute_angle = 360 * minute / 60 - 90
        second_angle = 360 * second / 60 - 90

        self.hour_hand_x = self.radius * 0.5 * cos(radians(hour_angle))
        self.hour_hand_y = self.radius * 0.5 * sin(radians(hour_angle))
        self.minute_hand_x = self.radius * 0.8 * cos(radians(minute_angle))
        self.minute_hand_y = self.radius * 0.8 * sin(radians(minute_angle))
        self.second_hand_x = self.radius * 0.9 * cos(radians(second_angle))
        self.second_hand_y = self.radius * 0.9 * sin(radians(second_angle))