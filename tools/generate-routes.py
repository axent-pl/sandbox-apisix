import yaml
import os
import sys

N = 100
dir = os.path.dirname(__file__)

SERVICE_NAMES = yaml.safe_load(
    open(f'{dir}/services-unique.yaml', 'r')).get('services')

def represent_multiline_string(dumper, data):
    """Custom representer for handling multiline strings."""
    if "\n" in data:
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)


def generate_apisix_config_yaml():
    TPL_CONFIG = open(f'{dir}/templates/apisix-decoupled/config.yaml', 'r').read()
    TPL_CONFIG_SERVICES = open(f'{dir}/templates/apisix-decoupled/services.yaml', 'r').read()
    TPL_CONFIG_ROUTES = open(f'{dir}/templates/apisix-decoupled/routes.yaml', 'r').read()

    config = yaml.safe_load(TPL_CONFIG)
    config['services'] = []
    config['routes'] = []
    for sid in range(N):
        service_name = SERVICE_NAMES[sid].strip()
        services = yaml.safe_load(
            TPL_CONFIG_SERVICES.format(service_name=service_name))
        routes = yaml.safe_load(
            TPL_CONFIG_ROUTES.format(service_name=service_name))
        config['services'].extend(services['services'])
        config['routes'].extend(routes['routes'])

    yaml.safe_dump(config, sys.stdout, sort_keys=False)


def generate_apisix_standalone_config_yaml():
    TPL_CONFIG = open(
        f'{dir}/templates/apisix-standalone/config.yaml', 'r').read()
    TPL_CONFIG_SERVICES = open(
        f'{dir}/templates/apisix-standalone/services.yaml', 'r').read()
    TPL_CONFIG_ROUTES = open(
        f'{dir}/templates/apisix-standalone/routes.yaml', 'r').read()

    config = yaml.safe_load(TPL_CONFIG)
    config['services'] = []
    config['routes'] = []
    for sid in range(N):
        service_id = sid+1
        service_name = SERVICE_NAMES[sid].strip()
        services = yaml.safe_load(
            TPL_CONFIG_SERVICES.format(service_name=service_name, service_id=service_id))
        routes = yaml.safe_load(
            TPL_CONFIG_ROUTES.format(service_name=service_name, service_id=service_id))
        config['services'].extend(services['services'])
        config['routes'].extend(routes['routes'])

    yaml.representer.SafeRepresenter.add_representer(str, represent_multiline_string)
    yaml.safe_dump(config, sys.stdout, sort_keys=False)
    print("#END")


def generate_kong_config_yaml():
    TPL_CONFIG = open(f'{dir}/templates/kong/config.yaml', 'r').read()
    TPL_CONFIG_SERVICES = open(
        f'{dir}/templates/kong/services.yaml', 'r').read()
    TPL_CONFIG_ROUTES = open(f'{dir}/templates/kong/routes.yaml', 'r').read()

    config = yaml.safe_load(TPL_CONFIG)
    config['services'] = []
    for sid in range(N):
        service_name = SERVICE_NAMES[sid].strip()
        services = yaml.safe_load(
            TPL_CONFIG_SERVICES.format(service_name=service_name))
        routes = yaml.safe_load(
            TPL_CONFIG_ROUTES.format(service_name=service_name))
        services['services'][0]['routes'] = routes['routes']
        config['services'].extend(services['services'])
    yaml.representer.SafeRepresenter.add_representer(str, represent_multiline_string)
    yaml.safe_dump(config, sys.stdout, sort_keys=False)


if __name__ == '__main__':
    N = int(sys.argv[1])
    GW = sys.argv[2]
    if GW == 'apisix-decoupled':
        generate_apisix_config_yaml()
    elif GW == 'apisix-standalone':
        generate_apisix_standalone_config_yaml()
    elif GW == 'kong-decoupled'  or GW == 'kong-standalone':
        generate_kong_config_yaml()
