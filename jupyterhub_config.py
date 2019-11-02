c = get_config()

from jupyter_client.localinterfaces import public_ips
import dockerspawner

ip = public_ips()[0]

c.JupyterHub.hub_ip = ip

c.JupyterHub.base_url = '/notebooks'
#c.JupyterHub.hub_ip = 'mammon.trade'

import os
path = os.path.dirname(os.path.abspath(__file__))
pjoin = os.path.join

runtime_dir = os.path.join('/srv/jupyterhub')
ssl_dir = pjoin(runtime_dir, 'ssl')
if not os.path.exists(ssl_dir):
  os.makedirs(ssl_dir)

sslDir = '/etc/letsencrypt/live/mammon.trade/'

c.JupyterHub.port = 443
c.JupyterHub.ssl_key = sslDir + 'privkey.pem'
c.JupyterHub.ssl_cert = sslDir + 'fullchain.pem'

c.JupyterHub.cookie_secret_file = pjoin(runtime_dir, 'cookie_secret')
c.JupyterHub.db_url = pjoin(runtime_dir, 'jupyterhub.sqlite')

c.JupyterHub.authenticator_class = 'jwtauthenticator.jwtauthenticator.JSONWebTokenAuthenticator'
c.JSONWebTokenAuthenticator.secret = 'ZEdWUWROQ0t4TTNjVnhiNFJzMmJLUVNLU29Xc1hlbHcK'
c.JSONWebTokenAuthenticator.username_claim_field = 'name'

c.Authenticator.whitelist = {'BrandtWP', 'SovietCommandantOtter', 'BWP'}
c.Authenticator.admin_users = {'BrandtWP'}
c.JupyterHub.spawner_class='dockerspawner.DockerSpawner'
c.DockerSpawner.remove_containers = True
c.DockerSpawner.remove = True

c.Spawner.args = ['--NotebookApp.tornado_settings={"headers":{"Content-Security-Policy": "frame-ancestors *"}}']

c.JupyterHub.tornado_settings = {
    'headers': {
        'Content-Security-Policy': "frame-ancestors '*'",
    }
}

c.DockerSpawner.image = 'quantitate/notebook:0.5'


notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan/work'
c.DockerSpawner.notebook_dir = notebook_dir

# Mount the real user's Docker volume on the host to the notebook user's
# notebook directory in the container
c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir }

# c.Spawner.default_url = '/{username}'
# c.Spawner.notebook_dir = '/'
