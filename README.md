# aria2

An Ansible role
to install and use [aria2](https://aria2.github.io/),
a lightweight multi-protocol & multi-source command-line download utility.

## Installation

Clone this repository to your ansible roles directory:

    mkdir roles/
    git clone git@github.com:ibuchanan/ansible-aria2.git roles/aria2

You can also optionally push the included `files/aria2_1.20.0-1_armhf.deb` to
your destination host and install it (has `libc-ares2` as a dependency) if
you're experiencing problems with HTTPS downloads.

## Usage

This role needs to be passed two variables:

    rpc_user: username
    rpc_password: password

for the remote control feature in the included rpc server for starting downloads.

For example, as a `playbook.yml` file:

    - hosts: servers
      roles:
         - { role: aria2, x: 42 }


## Build

```bash
pip install -r requirements.txt
molecule test
```

## Copyright

Copyright (c) 2016 Florian Heinle <launchpad@planet-tiax.de>
Copyright (c) 2019 Ian Buchanan <ibuchanan@atlassian.com> (https://developer.atlassian.com/blog/authors/ibuchanan/)

[MIT License](LICENSE) means
you can do what you like with this software,
as long as you include the required notices.
This permissive license contains
a patent license from the contributors of the code.
