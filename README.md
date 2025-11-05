# Workstation

This is a playbook for setting up a KDE workstation.

## Using kitchen-ci

You must have the following installed to automate this playbook:

- rubygem-test-kitchen
- rubygem-kitchen-ansible
- rubygem-kitchen-qemu

### Test image

You must provide your own image.  This repo supports qcow2 based images for use with the `kitchen-qemu` driver.

Suggestions: 

- kiwi
- mkosi

### Runing kitchen

The usual way: `kitchen test`
Quick way: `kitchen verify`
Setup: `kitchen converge`

## References

- https://kitchen.ci/docs/getting-started/introduction/
- https://github.com/neillturner/kitchen-ansible
- https://github.com/esmil/kitchen-qemu/
- https://docs.pytest.org/en/stable/
- https://testinfra.readthedocs.io/en/latest/index.html
- https://osinside.github.io/kiwi/
- https://mkosi.systemd.io/
