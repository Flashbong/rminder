import os
import datetime
from .getcfg import Conf
from .rmdjson import JsonHandler
from .format import RmdFormat

class Rmind():

    def __init__(self):
        script_dir = os.path.dirname(__file__)
        home_dir = os.path.abspath(os.path.join(script_dir, os.pardir))
        config_values = Conf(home_dir).load_config()

        note_dir = config_values[0]
        note_file = config_values[1]

        # self.note_active = os.path.join(home_dir,note_dir,note_file)
        self.note_active = os.path.join(home_dir,note_dir,note_file)
        self.jsonremind = JsonHandler(self.note_active)


        # if os.path.exists(self.note_active):
        #     self.read_note()
        # else:
        #     try:
        #         self.create_note()            
        #     except:
        #         os.makedirs(os.path.join(home_dir,note_dir))
        #         self.create_note()
        #     finally:
        #         self.read_note()

    def get_welcome(self):
        welcome_message = f'''
                        _           __         
   ________  ____ ___  (_)___  ____/ /__  _____
  / ___/ _ \/ __ `__ \/ / __ \/ __  / _ \/ ___/
 / /  /  __/ / / / / / / / / / /_/ /  __/ /    
/_/   \___/_/ /_/ /_/_/_/ /_/\__,_/\___/_/     
===============================================
Edit below in order to change contents
vi {self.note_active}
'''
        return welcome_message

    def write_new_message(self,**note_fields):
        creation_time = datetime.datetime.now()
        creation_time_str = creation_time.strftime("%Y-%m-%d %H:%M:%S")
        note = {
                "task_id": self.note_file,
		        "title": "Nowe features",
		        "creation_time": creation_time_str,
                "update_time": creation_time_str,
                "status": "Active",
                "priority": "Minor",
                "message": note_fields.pop['Lorem Ipsum']
        }
        return self.jsonremind.write_json(note)

    def read_note(self):
        note_dict = self.jsonremind.read_json()
        return RmdFormat(note_dict)


#     def create_note(self):
#         welcome_message = f'''
#                         _           __         
#    ________  ____ ___  (_)___  ____/ /__  _____
#   / ___/ _ \/ __ `__ \/ / __ \/ __  / _ \/ ___/
#  / /  /  __/ / / / / / / / / / /_/ /  __/ /    
# /_/   \___/_/ /_/ /_/_/_/ /_/\__,_/\___/_/     
# ===============================================
# Edit below in order to change contents
# vi {self.note_active}
# '''
#         with open(self.note_active, 'w') as file:
#             file.write(welcome_message)
#         return file.close()    

    # def read_note(self):
    #     with open(self.note_active, 'r') as file:
    #         print(file.read())
    #     return file.close()    
        

    def update_note(self):
        pass

    def delete_note(self):
        pass

    def format_response(self,data):
        formatted = str(f'''
======================================================
Task ID:\t\t\t\t{data['task_id']}
Title:\t\t\t\t\t{data['title']}              
Creation time:\t\t\t\t{data['creation_time']}    
Update time:\t\t\t\t{data['update_time']}
Status:\t\t\t\t\t{data['status']}
Priority:\t\t\t\t{data['priority']}
Message:\n\t{data['message']}
              ''')
        return print(formatted)