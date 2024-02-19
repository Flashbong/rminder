import os

class GetMessage():
    def __init__(self,home_dir) -> None:
        template_dir = str('templates')
        self.templates = os.path.join(home_dir, template_dir)


    def get_message(self):
        messages = (
            'welcome': 'welcome',
            'manpage': 'manpage',
            'credits': 'credits'
        )
        return messages