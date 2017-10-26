from common import _log, _print_fail, _print_success, _sys_call

class MySQL:
	def __init__(self):
		self.DB_HOST = 'localhost'
		self.DB_ROOT_USER = 'root'
		self.DB_ROOT_PASSWORD = 'rootp'
		self.DB_USER = 'asis'
		self.DB_USER_PASSWORD = 'asisp'
		self.DATABASE = 'asis'
		self.cmd_install = """
cat << EOF | debconf-set-selections
mysql-server mysql-server/root_password password rootp
mysql-server mysql-server/root_password_again password rootp
mysql-server mysql-server/root_password seen true
mysql-server mysql-server/root_password_again seen true
EOF
apt-get -y install mysql-server mysql-client
"""
		self.cmd_uninstall = "yum remove -y mysql-*"
		self.cmd_create_DB = "'CREATE DATABASE IF NOT EXISTS {0} CHARACTER SET utf8 COLLATE utf8_general_ci; GRANT ALL on {0}.* TO  {1}@localhost IDENTIFIED BY \"{2}\"; FLUSH PRIVILEGES;'".format(
            self.DATABASE, self.DB_USER, self.DB_USER_PASSWORD)

		self.cmd_execute = "mysql -u{0} -h{1} -p{2} -e {{0}}".format(
            self.DB_ROOT_USER, self.DB_HOST, self.DB_ROOT_PASSWORD)

	def install(self):
		_log(self.__class__.__name__, 'install')

		if _sys_call(self.cmd_install):
			_print_success(self.__class__.__name__)
		else:
			_print_fail(self.__class__.__name__)
			sys.exit()

	def uninstall(self):
		_log(self.__class__.__name__, 'uninstall')
		_sys_call(self.cmd_uninstall)

	def command(self, cmd):
		_log(self.__class__.__name__, 'execute command')
		print(cmd)
		_sys_call(self.cmd_execute.format(cmd))


	def create_DB(self):
		_log(self.__class__.__name__, 'create database')
		self.command(self.cmd_create_DB)

	def execute(self):
		self.install()
		self.create_DB()

	