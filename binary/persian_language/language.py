import yaml
import logging
def prep(config_file):
            parameters=config_reader(config_file)
        return sl
def config_reader( configFile):
            my_dict = yaml.safe_load(open(configFile))
            parameter = my_dict.get('parameter')
        return parameter
def detect():
        result="generate results"
        return result
