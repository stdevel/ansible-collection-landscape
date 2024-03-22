[![Build Status](https://travis-ci.org/stdevel/ansible-landscape.svg?branch=master)](https://travis-ci.org/stdevel/ansible-landscape)

# landscape

This role prepares and installs [Canonical Landscape](https://landscape.canonical.com/).

## Requirements

The system needs access to the internet. Also, you will need an prober Ubuntu release:

| Landscape version | Supported Ubuntu verions |
| ----------------- | ------------------------ |
| 23.03 | Ubuntu 20.04 (*Focal Fossa*) or 22.04 (*Jammy Jellyfish*) |
| 23.10 | Ubuntu 20.04 (*Focal Fossa*) or 22.04 (*Jammy Jellyfish*) |

## Role variables

| Variable | Default | Description |
| -------- | ------- | ----------- |
| `landscape_version` | `23.03` | Landscape version to install (*see above*) |
| `landscape_core_packages` | see [`defaults`](defaults/main.yml) | Core packages to install |
| `landscape_ppa` | `ppa:landscape/version` | Landscape PPA URL |
| `landscape_packages` | see [`defaults`](defaults/main.yml) | Landscape packages to install |
| `landscape_use_lvm` | `true` | Use LVM for application data |
| `landscape_vg` | `vg_landscape` | Volume Group name |
| `landscape_pv` | `/dev/sdb` | Disk to use for application data |
| `landscape_filesystems` | see [`defaults`](defaults/main.yml) | Application data filesystems to create |

## Dependencies

No dependencies.

## Example playbook

Refer to the following example:

```yaml
---
- hosts: servers
  roles:
    - stdevel.landscape
```

Set variables if required, e.g. for dedicated software repository filesystem:

```yaml
---
- hosts: landscape.giertz.loc
  roles:
    - role: stdevel.landscape
      landscape_filesystems:
        - name: lv_pgsql
          type: xfs
          mountpoint: /var/lib/postgresql
          size: 5120
        - name: lv_landscape
          type: xfs
          mountpoint: /var/lib/landscape
          size: 20480
        - name: lv_repository
          type: xfs
          mountpoint: /var/lib/landscape/landscape-repository
          size: 102400
```

If you're really into old software, you can also install [unsupported versions](https://launchpad.net/~landscape) for your museum:

```yaml
---
- hosts: pepperidge.farm.loc
  roles:
    - role: stdevel.landscape
      landscape_version: '19.10'
      landscape_ppa: "ppa:landscape/19.10"
      landscape_packages:
        - landscape-server-quickstart
        - landscape-api
```

## License

Apache 2.0

## Author information

Christian Stankowic (info@cstan.io)
