# molecule

This folder contains molecule configuration and tests.

## Preparation

Ensure to the following installed:

- [Vagrant](https://vagrantup.com)
- [Oracle VirtualBox](https://virtualbox.org)
- Python modules
  - [`molecule`](https://pypi.org/project/molecule/)
  - [`molecule-vagrant`](https://pypi.org/project/molecule-vagrant/)
  - [`python-vagrant`](https://pypi.org/project/python-vagrant/)

## Environment

The test environment consists of one test scenario:

- `default` - default scenario with a VM running Ubnutu

## Usage

In order to create the test environment execute the following command:

```shell
$ molecule create
```

Also, spin up a Landscape server and alter the IP address in [`converge.yml`](converge.yml):

```yaml
...
  pre_tasks:
    - name: Set hosts entry for local Landscape server
      ansible.builtin.lineinfile:
        path: /etc/hosts
        line: '192.168.124.106 landscape-server-2310'
```

Run the Ansible role:

```shell
$ molecule converge
```

Finally, run the tests:

```shell
$ molecule verify
```
