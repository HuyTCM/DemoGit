from common import _log, _print_fail, _print_success, _sys_call

class NGINX(object):
	"""docstring for NGINX"""
	def __init__(self):
		super(NGINX, self).__init__()
		self.cmd_install = "apt-get install -y nginx"

	def install(self):
		_log(self.__class__.__name__, 'install')
		print('uninstall')
		if _sys_call(self.cmd_install):
			_print_success(self.__class__.__name__)
		else:
			_print_fail(self.__class__.__name__)
			sys.exit()