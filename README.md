# landscape

This role prepares and installs [Canonical Landscape](https://landscape.canonical.com/).

## Requirements

The system needs access to the internet. Also, you will need Ubuntu 16.04 (*Xenial Xerus*) or 18.04 (*Bionic Beaver*).

## Role variables


| Variable | Default | Description |
| -------- | ------- | ----------- |
| `landscape_version` | `19.10` | Landscape version to install |
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

## License

Apache 2.0

## Author information

Christian Stankowic (info@cstan.io)
