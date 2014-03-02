#!/usr/bin/env python
import sys

from django.conf import settings
from django.core.management import execute_from_command_line


if not settings.configured:
    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
            }
        },
        INSTALLED_APPS=(
            ## if you use auth.User:
            #'django.contrib.auth',
            ## if you use contenttypes
            # 'django.contrib.contenttypes',
            'my_app',
            'tests',
        ),
        TEST_RUNNER='django_nose.NoseTestSuiteRunner',
        # etc
    )


def runtests():
    argv = sys.argv[:1] + ['test', 'tests']
    execute_from_command_line(argv)


if __name__ == '__main__':
    runtests()
