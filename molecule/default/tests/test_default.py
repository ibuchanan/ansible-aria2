import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_download_dir(host):
    download_dir = host.file('/tmp/atlassian-downloads')

    assert download_dir.exists
    assert download_dir.is_directory
    assert download_dir.user == 'atlassian'
    assert download_dir.group == 'atlassian'
    assert download_dir.mode == 0o754
