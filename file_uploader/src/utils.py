import configparser


def get_config(config_file_path, section, key):

    config = configparser.ConfigParser()
    config.read(config_file_path)
    return config[section][key]