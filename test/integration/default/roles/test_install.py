# test_install.py

"""
roles/install/tasks/main.yml
"""

import pytest
import yaml

def read_yaml(file):
    """Reads in a yaml
    and outputs a dict
    """
    with open(file, "r") as f:
        _data = yaml.load(f, yaml.SafeLoader)
    return _data


ROLEPATH = "roles/install"
PKGS = read_yaml(f"{ROLEPATH}/tasks/main.yml")[1]["ansible.builtin.dnf"]["name"]


@pytest.mark.xfail(reason="modularity test is for centos only")
def test_install_ruby_modularity__package_version(host):
    """
    Verify package is installed

    This test checks the version of a package installed
    via modularity plugin.
    """
    assert host.package("ruby").version == '3.1.7'


@pytest.mark.parametrize("pkgs", PKGS)
def test_install_core_workstation_packages__package_installed(host, pkgs):
    """ Verify packages are installed """
    assert host.package(pkgs).is_installed
