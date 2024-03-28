# storage

This role prepares and configures storage for [Ubuntu Landscape](https://ubuntu.com/landscape).

## Requirements

No requirements.

## Role Variables

| Variable | Default | Description |
| -------- | ------- | ----------- |
| `storage_vg` | `landscape` | LVM volume group to create for Docker data |
| `storage_pv` | `/dev/sdb` | Disk to use for LVM |
| `storage_filesystems` | see [defaults/main.yml](defaults/main.yml) | LVs, filesystems and mount points to create |

## Dependencies

No dependencies.

## Example Playbook

Refer to the following example:

```yaml
- hosts: servers
  roles:
    - stdevel.landscape.storage
```

Set variables if required, e.g.:

```yaml
---
- hosts: landscape.giertz.loc
  remote_user: root
  roles:
    - role: stdevel.landscape.storage
      storage_vg: vg_landscape
      storage_pv: /dev/sdb
      storage_filesystems:
        - name: lv_pgsql
          type: xfs
          mountpoint: /var/lib/postgresql
          size: 10240
        - name: lv_landscape
          type: xfs
          mountpoint: /var/lib/landscape
          size: 40960
```

## License

GPL 3.0

## Author Information

Christian Stankowic (info@cstan.io)
