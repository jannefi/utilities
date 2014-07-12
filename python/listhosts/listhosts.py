#!/usr/bin/env python
import socket
import sys

"""	
	listhosts, a simple Python command line utility
	
	Prints the host addresses of each domain listed in a file
	
	Author: Janne Ahlberg
	
	Revision history
	- 12-Jul-2014		first revision
	
"""

class ListHosts:
	""" ListHosts class """
	domains = []
	
	def read_domains(self, file_name):
		""" read domain names from a text file 
		"""
		try:
			text_file = open(file_name, "r")
		except:
			print "Failed to open input file %s" % (file_name)
			exit(1)
		self.domains = text_file.readlines()
		text_file.close()

	def print_hosts(self):
		""" gets the host address for each domain and prints it 
		"""
		text_out = "%s has address: %s"
	
		for domain in self.domains:
			domain = domain.strip()
			try:
				ip_number = socket.gethostbyname(domain)
			except:
				ip_number = "failed!"
		
			print text_out % (domain, ip_number)

class Main:
	""" Main class - similar to main() function in C """
	def usage(self):
		print "Usage: python listhosts.py filename"
		
	def __init__(self, argv):
		""" init function
		"""
		try:
			file_name = argv[0]
		except:
			self.usage()
			exit(1)
		
		x = ListHosts()
		x.read_domains(file_name)
		x.print_hosts()
		
if __name__ == "__main__":
	x = Main(sys.argv[1:])
