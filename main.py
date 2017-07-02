#!/usr/bin/env python3

import os
from os.path import join, dirname
from dotenv import load_dotenv

from pprint import pprint as pp

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

LDAP_SERVER = os.environ.get("LDAP_SERVER").strip()
LDAP_USERS  = [x.strip() for x in os.environ.get("LDAP_USERS").split(',')]


