# utils/time_tracker.py
from kivy.clock import Clock

class TimeTracker:
    def __init__(self):
        self.alarm_interval = 60 * 60 * 3  # 3 години
        self.clock_event = None

    def start_alarm(self, callback):
        if self.clock_event:
            self.clock_event.cancel()
        self.clock_event = Clock.schedule_interval(callback, self.alarm_interval)

    def stop_alarm(self):
        if self.clock_event:
            self.clock_event.cancel()
