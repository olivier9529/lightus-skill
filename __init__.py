from mycroft import MycroftSkill, intent_file_handler


class Lightus(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('lightus.intent')
    def handle_lightus(self, message):
        self.speak_dialog('lightus')


def create_skill():
    return Lightus()

