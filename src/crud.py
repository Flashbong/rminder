import os
import yaml

class Rmind():

    def __init__(self):
        script_dir = os.path.dirname(__file__)
        home_dir = os.path.abspath(os.path.join(script_dir, os.pardir))
        config_values = self.get_config(home_dir)

        note_dir = config_values[0]
        note_file = config_values[1]

        self.note_active = os.path.join(home_dir,note_dir,note_file)


        if os.path.exists(self.note_active):
            self.read_note()
        else:
            try:
                self.create_note()            
            except:
                os.makedirs(os.path.join(home_dir,note_dir))
                self.create_note()
            finally:
                self.read_note()

        # if os.path.exists(home_dir):
        #     self.create_note()

        # if not os.path.exists(self.note_active):
        #     os.makedirs(os.path.join(home_dir,note_dir))
        #     self.create_note()


    def get_config(self,home_dir):
        config_dir = str('config')
        config_file = str('config.yaml')
        config_path = os.path.join(home_dir, config_dir, config_file)
        with open(config_path, "r") as file:
            config_data = yaml.load(file, Loader=yaml.FullLoader)
            int_db_config = config_data['reminder']['local-db-data']
            ext_db_config = config_data['reminder']
            if int_db_config['local-db'] == True:
                note_dir = int_db_config['note-db']
                note_file = int_db_config['note-prefix']+'02'
                local_configuration = (note_dir,note_file) 
            if ext_db_config == True:
                pass
            else:
                pass
            file.close()
        return local_configuration

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