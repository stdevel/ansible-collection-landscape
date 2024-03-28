"""
Molecule unit tests
"""
from __future__ import absolute_import, division, print_function
__metaclass__ = type
import os
import testinfra.utils.ansible_runner

TESTINFRA_HOSTS = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_packages(host):
    """
    Check if required packages are installed
    """
    server_packages = [
        'landscape-client'
    ]
    # check dependencies and Landscape packages
    for pkg in server_packages:
        assert host.package(pkg).is_installed

def test_initialization(host):
    """
    Check if client was initialized properly
    """
    # check database
    _database = host.file("/var/lib/landscape/client/manager.database")
    assert _database.exists

    # check configuration
    with host.sudo():
        _config = host.file("/etc/landscape/client.conf")
        assert _config.exists
        assert _config.contains('https://landscape.canonical.com') is False
        for _key in ['url', 'ping_url', 'data_path']:
            assert _config.contains(f"{_key} =")
