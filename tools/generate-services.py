import randomname
import yaml
import os

N = 10000

service_names = [ randomname.get_name(adj=('music_theory',), noun=('cats', 'food')) for _ in range(N) ]
services = {
    'services': service_names
}

dir = os.path.dirname(__file__)
with open(f'{dir}/services.yaml','w') as rf:
    yaml.safe_dump(services,rf)