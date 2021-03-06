# (C) Datadog, Inc. 2018
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

import os

import pytest

from datadog_checks.dev import docker_run

from .common import HERE, HOST, PORT


@pytest.fixture(scope="session")
def dd_environment():
    with docker_run(compose_file=os.path.join(HERE, "compose", "docker-compose.yml"), sleep=10):
        yield


@pytest.fixture
def instance():
    return {
        'default_timeout': 5,
        'tag_by_url': True,
        'url': 'http://{}:{}/stats'.format(HOST, PORT),
        'name': 'testInstance',
        'json_path': ['*', '*.*', '*.*.*', '*.*.*.*'],
    }
