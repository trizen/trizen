#!/usr/bin/env python

# The MIT License (MIT)
#
# Copyright (c) 2017 Plague Doctor
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software, to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, distribute,
# sub-license, and/or sell copies of the Software, and to permit persons to whom
# the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# This module is a re-written version of the pacaur.py module by Austin Hyde.


from ansible.module_utils.basic import *


def trizen_available(module):
    rc, stdout, stderr = module.run_command('which trizen', check_rc=False)
    return rc == 0


def pacman_available(module):
    rc, stdout, stderr = module.run_command('which pacman', check_rc=False)
    return rc == 0


def package_installed(module, pkg):
    rc, stdout, stderr = module.run_command('pacman -Q {}'.format(pkg), check_rc=False)
    return rc == 0


def check_packages(module, pkgs, state):
    global packages
    would_be_changed = []
    action = 'installed'

    for pkg in packages:
        installed = package_installed(module, pkg)
        if (state == 'present' and not installed) or (state == 'absent' and installed):
            would_be_changed.append(pkg)

    if state == 'absent':
        action = 'removed'

    if would_be_changed:
        module.exit_json(changed=True, msg='{no_of_packages} package(s) would be {act}.'.format(no_of_packages=len(would_be_changed), act=action))
    else:
        module.exit_json(changed=False, msg='all packages are already {act}.'.format(act=action))


def install_packages(module, pkgs):
    num_installed = 0

    cmd = 'trizen --quiet --noconfirm -S {pkg_name}'

    for pkg in pkgs:
        if package_installed(module, pkg):
            continue

        rc, stdout, stderr = module.run_command(cmd.format(pkg_name=pkg), check_rc=False)

        if rc != 0:
            module.fail_json(msg='failed to install package {pkg_name}, because: {err}.'.format(pkg_name=pkg, err=stderr))

        num_installed += 1

    if num_installed > 0:
        module.exit_json(changed=True, msg='installed {} package(s).'.format(num_installed))
    else:
        module.exit_json(changed=False, msg='all packages were already installed.')


def remove_packages(module, pkgs, recurse):
    num_removed = 0

    arg = 'R'
    action = 'remove'
    if recurse:
        arg = 'Rs'
        action = 'recursively remove'

    cmd = 'pacman -{argument} --noconfirm {pkg_name}'

    for pkg in pkgs:
        if not package_installed(module, pkg):
            continue

        rc, stdout, stderr = module.run_command(cmd.format(argument=arg, pkg_name=pkg), check_rc=False)

        if rc != 0:
            module.fail_json(msg='failed to {act} package {pkg_name} because: {err}.'.format(act=action, pkg_name=pkg, err=stderr))

        num_removed += 1

    if num_removed > 0:
        module.exit_json(changed=True, msg='removed {no_of_packages} package(s).'.format(no_of_packages=num_removed))
    else:
        module.exit_json(changed=False, msg='all packages were already removed.')


def main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            state=dict(default='present', choices=['present', 'absent']),
            recurse=dict(default='no', choices=BOOLEANS, type='bool')
        ),
        supports_check_mode=True
    )

    if not trizen_available(module):
        module.fail_json(msg="could not locate trizen...")

    if not pacman_available(module):
        module.fail_json(msg="could not locate pacman...")

    p = module.params

    pkgs = p['name'].split(',')

    if module.check_mode:
        check_packages(module, pkgs, p['state'])

    if p['state'] == 'present':
        install_packages(module, pkgs)
    elif p['state'] == 'absent':
        remove_packages(module, pkgs, p['recurse'])


if __name__ == '__main__':
    main()
