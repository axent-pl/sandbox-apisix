import randomname
import yaml
import os

N = 1000
dir = os.path.dirname(__file__)

SERVICE_NAMES = yaml.safe_load(
    open(f'{dir}/services.yaml', 'r')).get('services')
TPL_CONFIG = open(f'{dir}/templates/config.yaml', 'r').read()
TPL_CONFIG_SERVICES = open(f'{dir}/templates/services.yaml', 'r').read()
TPL_CONFIG_ROUTES = open(f'{dir}/templates/routes.yaml', 'r').read()


def generate_config_yaml():
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

    with open(f'{dir}/routes-{N}.yaml', 'w') as rf:
        yaml.safe_dump(config, rf, sort_keys=False)


if __name__ == '__main__':
    generate_config_yaml()
