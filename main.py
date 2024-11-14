from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.lang import Builder
from screens.home_screen import HomeScreen
from screens.alarm_screen import AlarmScreen
from screens.settings_screen import SettingsScreen
from utils.clock_widget import ClockWidget  # Import ClockWidget

class ClockScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class ReminderApp(App):
    def build(self):
        Builder.load_file('kv_files/home_screen.kv')
        Builder.load_file('kv_files/alarm_screen.kv')
        Builder.load_file('kv_files/settings_screen.kv')
        Builder.load_file('kv_files/clock.kv')

        wm = WindowManager(transition=NoTransition())
        wm.add_widget(HomeScreen(name="home"))
        wm.add_widget(AlarmScreen(name="alarm"))
        wm.add_widget(SettingsScreen(name="settings"))
        wm.add_widget(ClockScreen(name="clock"))
        wm.current = "home"  # Default screen
        return wm

if __name__ == "__main__":
    ReminderApp().run()