
class RmdFormat(note_dict):
    def __init__(note_dict):
        format_reponse = str(f'''
======================================================
Task ID:\t\t\t\t{note_dict['task_id']}
Title:\t\t\t\t\t{data['title']}              
Creation time:\t\t\t\t{data['creation_time']}    
Update time:\t\t\t\t{data['update_time']}
Status:\t\t\t\t\t{data['status']}
Priority:\t\t\t\t{data['priority']}
Message:\n\t{data['message']}
              ''')
        return print(format_reponse)