import subprocess
import sys

def _sys_call(args):
    status = subprocess.call(args, shell=True)
    if status == 0:
        return True
    else:
        return False

def _log(arg, action):
	print("[+++] {0}: {1}".format(arg, action))

def _print_success(arg):
    print("[+] {0}: successed".format(arg))


def _print_fail(arg):
    print("[-] {0}: failed".format(arg))
