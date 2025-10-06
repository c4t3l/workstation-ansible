# test_repos.py

"""
roles/repos/tasks/main.yml
"""

from docitlib import read_file

ROLEPATH = "roles/repos"
LOC_REPO_FILE = f"{ROLEPATH}/files/workstation.repo"
REM_REPO_FILE = "/etc/yum.repos.d/workstation.repo"


def test_deploy_local_configs__file_exists(host):
    """Verify file exists"""
    assert host.file(REM_REPO_FILE).exists


def test_deploy_local_configs__file_content(host):
    """Verify file content"""
    assert host.file(REM_REPO_FILE).content_string == read_file(LOC_REPO_FILE)


def test_deploy_local_configs__file_user(host):
    """Verify file user"""
    assert host.file(REM_REPO_FILE).user == "root"


def test_deploy_local_configs__file_group(host):
    """Verify file group"""
    assert host.file(REM_REPO_FILE).group == "root"
