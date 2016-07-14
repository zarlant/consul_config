Role Name
=========

Create consul user and group and sets up consul configuration for use under either Docker or installed normally on the server.

Role Variables
--------------

Everything lives in defaults/main in the role. Everything can be overridden, but for the most part defaults will do.

Example Playbook
----------------

	- name: Ensure registrator and consul are running
	  hosts: "docker-{{env}}"
	  vars_files:
	   - vars/main.yml
	  roles:
	    - consul_config

License
-------

BSD

Author Information
------------------
Zacharias Thompson @zarlant <zarlant@gmail.com>
