"""
Unit tests
"""
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
        'landscape-server-quickstart'
    ]
    # check dependencies and Landscape packages
    for pkg in server_packages:
        assert host.package(pkg).is_installed


def test_ports_listen(host):
    """
    Check if application ports are listening
    """
    for port in [80, 443, 8080]:
        assert host.socket("tcp://0.0.0.0:%s" % port).is_listening
