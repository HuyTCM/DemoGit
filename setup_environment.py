import shutil
from common import _sys_call

from mysql_setup import MySQL
from nginx_setup import NGINX
from uwsgi_setup import uWSGI

def main():
    SOURCE_PATH = "./"

    # # update apt-get first
    # _sys_call("apt-get -qy install update")
    # _sys_call("apt-get -qy install python-dev python3-pip --fix-missing")

    # install source's requirement
    _sys_call("pip3 install -r requirements.txt")

    # # set-up mysql
    # mySQL = MySQL()
    # mySQL.execute()

    # # set-up nginx
    # nginx = NGINX()
    # nginx.install()

    # # set-up uwsgi
    uwsgi = uWSGI()
    # uwsgi.install()
    uwsgi.copy_config_file(SOURCE_PATH)

    # copy conf file to /etc/init/
    shutil.copy('asis.conf', "/etc/init/")
    _sys_call("start asis")

    # copy nginx config
    shutil.copy('asis', "/etc/nginx/sites-available/")
    _sys_call('ln -s /etc/nginx/sites-available/asis /etc/nginx/sites-enabled/asis')
    _sys_call("service nginx restart")

main()
