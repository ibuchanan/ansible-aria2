import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_aria2c_exists(host):
    assert host.exists('aria2c')
    assert host.run_test('aria2c --version')
