# test_install.py

"""
roles/install/tasks/main.yml
"""

import pytest
from docitlib import read_yaml

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
