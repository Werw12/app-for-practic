# screens/alarm_screen.py
from kivy.uix.screenmanager import Screen
from utils.time_tracker import TimeTracker
from plyer import notification

class AlarmScreen(Screen):
    def on_enter(self):
        # Запуск будильника кожні 3 години
        self.tracker = TimeTracker()
        self.tracker.start_alarm(self.show_notification)

    def show_notification(self, dt):
        notification.notify(
            title="Перерва!",
            message="Час зробити перерву та розім'яти очі!",
            timeout=10
        )
