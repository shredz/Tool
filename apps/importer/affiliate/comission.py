from settings import CJPERL

import subprocess

class CJ:
	def __init__(self):
		pass
	
	@staticmethod
	def get_real_reports():
		pass
	
	@staticmethod
	def get_deals():
		return subprocess.Popen([r"perl", CJPERL+"uireplace.pl","2637633, 2637635, 2637628, 2637624"], stderr=subprocess.PIPE, stdout=subprocess.PIPE).communicate()[0]
