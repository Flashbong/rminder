import json
import datetime

class Json_remind():
    def __init__(self, note) -> None:  
        meta_block = note['meta_block'][0]
        self.task_id=meta_block['task_id']
        self.task_name=meta_block['task_name']
        self.note_creation=meta_block['note_creation']
        self.last_update=meta_block['task_last_update']

        note_block = note['meta_block'][0]
        self.status = note_block['status']
        self.note_priority = note_block['priority']
        self.note_message = note_block['message']
    
    def json_read(self):
        print('''
    Task ID:\t\t\t
    Task title:\t\t\t
    Task creation:\t\t\t
    Last update:\t\t\t
    ================================================
    Status:\t\t\t

    Priority:\t\t\t
    Contents:\t\t\t
              ''')

    def json_write(self):

        meta_block = {
            'task_id': task_id,
            'task_name': task_title,
            'task_creation': datetime.datetime.now(),
            'task_last_update': datetime.datetime.now(),
        }

        note_block = {
            'status': note_status,
            'priority': note_priority,
            'message': note_message,
        }

        note {
            meta_block,
            note_block,
        }
        return

    def json_update(self, note):
        note['meta_block'][0]['task_last_update'] = datetime.datetime.now()
        return 