import datetime
import json
import os
from getpass import getuser
from StringIO import StringIO
from fabric.api import env, run, local, cd, abort, lcd, get
import globaltraining


# env.project_git = 'mb-global_training_backend' #git checkout
env.project = 'mattermost'
env.namespace = 'mm'
env.repository = 'https://github.com/domenikjones/mm-hub.git'
#env.repository = 'gitlab.s-v.de:%(namespace)s/%(project_git)s.git' % env
env.project_root = os.path.dirname(os.path.abspath(__file__))
# env.forward_agent = True


# ------ environments ----------
def digitalocean():
    env.hosts = ['root@138.68.89.118']
    env.environment = 'master'
    env.database_user = 'root'
    env.database_name = ''
    env.database_host = 'localhost'
    env.database_password = ''
    # env.site_url = 'dev.globaltraining.d.s-v.de'




def update_dependencies():
    run("%(environment)s/bin/pip install --requirement "
        "%(environment)s/src/%(project)s/requirements/%(environment)s.txt" % env)


def reload(extra_msg=None):
    run("kill -HUP `cat %(environment)s/run/gunicorn.pid`" % env)


def migrate():
    run("%(environment)s/bin/django-admin.py migrate "
        "--settings=%(project)s.conf.%(environment)s" % env)


def run_aggregators():
    run("%(environment)s/bin/django-admin.py aggregate_trainings "
        "--settings=%(project)s.conf.%(environment)s" % env)


def deploy():
    run('%(environment)s/bin/django-admin.py collectstatic '
        '--settings=%(project)s.conf.%(environment)s --noinput' % env)
    # add potentially missing permissions
    run('%(environment)s/bin/django-admin.py fix_permissions '
        '--settings=%(project)s.conf.%(environment)s' % env)
    run('crontab %(environment)s/src/%(project)s/deployment/%(host)s/crontab' % env)
    # compile locale files
    with cd('%(environment)s/src/%(project)s/%(project)s' % env):
        run('~/%(environment)s/bin/django-admin.py compilemessages' % env)
    migrate()
    # set group permissions
    run('%(environment)s/bin/django-admin.py update_group_permissions '
        '--settings=%(project)s.conf.%(environment)s' % env)
    reload()
    #TODO: notify removed