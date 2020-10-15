from __future__ import absolute_import
import os
import sys

# When defaults are loaded assume a local development environment
# All other environments should explicitly choose a right settings
try:
    explicitly_chosen_env_settings = os.environ.get('DJANGO_SETTINGS_MODULE').split('.')[2]
    possible_env_settings = ['local', 'test', 'production']
    if explicitly_chosen_env_settings is None or explicitly_chosen_env_settings not in possible_env_settings:
        sys.stderr.write("Error: Can't find the file %r in the directory settings." % os.environ.get('DJANGO_SETTINGS_MODULE'))
        sys.exit(1)
    else:
        pass

except IndexError:
    from .local import *
    sys.stdout.write("Info: defaults settings file is loaded assume a local development environment.\n")
