import yaml
import os

class Conf:
    def __init__(self, home_dir):
        config_dir = str('config')
        config_file = str('config.yaml')
        self.config_path = os.path.join(home_dir, config_dir, config_file)

    def load_config(self):
        with open(self.config_path, "r") as file:
            config_data = yaml.load(file, Loader=yaml.FullLoader)
            int_db_config = config_data['reminder']['local-db-data']
            ext_db_config = config_data['reminder']

            if int_db_config['local-db'] == True:
                note_dir = int_db_config['note-db']
                note_file = int_db_config['note-prefix']+'.json'
                local_configuration = (note_dir,note_file)

            if ext_db_config == True:
                pass

            else:
                pass

            file.close()

        return local_configuration