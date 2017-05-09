from __future__ import absolute_import
import os
from apollo import ApolloInstance
from .config import read_global_config, global_config_path


def get_instance(instance_name=None):
    # I don't like reading the config twice.
    conf = read_global_config()
    if not os.path.exists(global_config_path()):
        # Probably creating the file for the first time.
        return None

    if instance_name is None or instance_name == '__default':
        try:
            instance_name = conf['__default']
        except KeyError:
            raise Exception("Unknown Apollo instance and no __default provided")

    if instance_name not in conf:
        raise Exception("Unknown Apollo instance; check spelling or add to ~/.apollo-arrow.yml")

    return conf[instance_name]


def get_apollo_instance(instance_name=None):
    conf = get_instance(instance_name=instance_name)
    return ApolloInstance(conf['url'], conf['username'], conf['password'])
