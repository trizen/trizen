*trizen.py* is an ansible module to use trizen aur helper.

## Usage

1. Add the module to your playbook:

   ```
   mkdir -p library
   wget -o library/trizen.py https://raw.githubusercontent.com/trizen/trizen/master/ansible/trizen.py
   ```


2. Use it in a task, as in the following examples:

   ```
   - name: "Install package using trizen."
     become_user: <some_user_that_has_nopasswd_in_sudoers_for_pacman_use>
     package:
       name: <package-name>
       state: present
       use: trizen

   - name: "Install multiple packages using trizen."
     become_user: <some_user_that_has_nopasswd_in_sudoers_for_pacman_use>
     package:
       name: "{{ item }}"
       state: present
       use: trizen
     with_items:
       - <package1>
       - <package2>
       - <package3>

   - name: "Remove package using trizen."
     become_user: <some_user_that_has_nopasswd_in_sudoers_for_pacman_use>
     package:
       name: <package-name>
       state: absent
       use: trizen
   ```
