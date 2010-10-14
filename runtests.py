#!/usr/bin/env python
import os, sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
parent = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, parent)

from django.test.simple import run_tests


def runtests():
    failures = run_tests(
        [
            'autofixture',
            'autofixture_tests',
            'autofixture_test',
            'generator_test',
            'sample_app',
        ],
        verbosity=1, interactive=True)
    sys.exit(failures)

if __name__ == '__main__':
    runtests()
