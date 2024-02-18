import os

class Rmind():

    def __init__(self):

        script_dir = os.path.dirname(__file__).parent
        note_dir = str('notebook_db')
        note_file = str('note-00')
        self.note_active = os.path.join(script_dir,note_dir,note_file)
        if not os.path.exists(self.note_active):
            os.makedirs(os.path.join(script_dir,note_dir))
            self.create_note()
        return self.read_note()

    def create_note(self):
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
        with open(self.note_active, 'w') as file:
            file.write(welcome_message)
        return file.close()    

    def read_note(self):
        with open(self.note_active, 'r') as file:
            print(file.read())
        return file.close()    
        

    def update_note(self):
        pass

    def delete_note(self):
        pass