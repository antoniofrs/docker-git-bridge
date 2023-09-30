import logging

def validate_config(config):
    assert_not_null(config["repo_url"], "DGB_GIT_REPO_URL")

def assert_not_null(value, env_var):
    if value == None:
        logging.info(f"{env_var} cannot be null")
        exit(1)

def convert_mapped_ports(ports):

    if ports == None:
        return None

    pairs = ports.split(',')
    result = {}
    for pair in pairs:
        key, value = pair.split(':')
        result[key] = value
    return result

def not_empty(stringa):
    if stringa is None:
        return False
    elif stringa.strip() == "":
        return False
    else:
        return True