import shutil
from common import _log, _print_fail, _print_success, _sys_call

class uWSGI(object):
	"""docstring for uWSGI"""
	def __init__(self):
		super(uWSGI, self).__init__()
		self.cmd_install = "pip3 install uwsgi"

	def install(self):
		_sys_call(self.cmd_install)

	def copy_config_file(self, destination_path): 
		shutil.copy('asis.ini', destination_path)