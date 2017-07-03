#!/usr/bin/env python3

import os, sys
from os.path import join, dirname
from dotenv import load_dotenv

from ldap3 import Server, Connection, SUBTREE

from pprint import pprint as pp

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

LDAP_SERVER = os.environ.get("LDAP_SERVER").strip()
LDAP_USERS  = [x.strip() for x in os.environ.get("LDAP_USERS").split(',')]
LDAP_BASEDN = os.environ.get("LDAP_BASE_DN").strip()

server = Server(LDAP_SERVER)
conn = Connection(server)
if conn.bind():
	conn.search(search_base=LDAP_BASEDN, search_filter="(objectclass=user)", search_scope=SUBTREE,attributes=['cn', 'memberOf'])
	total_entries += len(c.response)
	for entry in c.response:
	    print(entry['dn'], entry['attributes'])
else:
	print("Failed to bind connection")
	sys.exit(1)

sys.exit(0)
