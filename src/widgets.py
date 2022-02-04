from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.picker import MDDatePicker
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.anchorlayout import AnchorLayout


class RootWidget(ScreenManager):
    pass


class NextStep(AnchorLayout):
    def slide_to_next(self):
        sm = MDApp.get_running_app().root
        names = sm.screen_names
        idx = names.index(sm.current_screen.name)
        next_idx = (idx + 1) % len(names)
        sm.current = names[next_idx]


class GameButton(MDFillRoundFlatButton, MDToggleButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_down = self.theme_cls.primary_light


class DateInput(MDTextField):
    def open_date_picker(self):
        picker = MDDatePicker(
            title="選擇時間",
            title_input="輸入時間",
            font_name="font/Noto_Sans_TC/NotoSansTC-Bold.otf",
        )
        picker.bind(on_save=self.on_save)
        picker.open()

    def on_focus(self, instance, value):
        if value:
            super().on_focus(instance, value)
            self.open_date_picker()

    def on_save(self, instance, value, date_range):
        self.text = value.strftime("%Y-%m-%d")
        MDApp.get_running_app().select_range(self.hint_text, value)
