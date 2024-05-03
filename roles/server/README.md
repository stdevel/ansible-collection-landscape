# server

This role prepares and installs [Ubuntu Landscape](https://landscape.canonical.com/).

## Requirements

The system needs access to the internet. Also, you will need an prober Ubuntu release:

| Landscape version | Supported Ubuntu verions |
| ----------------- | ------------------------ |
| 24.04 | 22.04 (*Jammy Jellyfish*) or 24.04 (*Noble Numbat*) |
| 23.03 | Ubuntu 20.04 (*Focal Fossa*) or 22.04 (*Jammy Jellyfish*) |
| 23.10 | Ubuntu 20.04 (*Focal Fossa*) or 22.04 (*Jammy Jellyfish*) |

## Role variables

| Variable | Default | Description |
| -------- | ------- | ----------- |
| `server_version` | `24.04` | Landscape version to install (*see above*) |
| `server_ppa` | `ppa:landscape/version` | Landscape PPA URL |
| `server_packages` | see [`defaults`](defaults/main.yml) | Landscape packages to install |

## Dependencies

No dependencies.

## Example playbook

Refer to the following example:

```yaml
---
- hosts: servers
  roles:
    - stdevel.landscape.server
```

Set variables if required, e.g. for beta releases:

```yaml
---
- hosts: break.things.loc
  roles:
    - role: stdevel.landscape.server
      server_ppa: "ppa:landscape/self-hosted-beta"
```

If you're really into old software, you can also install [unsupported versions](https://launchpad.net/~landscape) for your museum:

```yaml
---
- hosts: pepperidge.farm.loc
  roles:
    - role: stdevel.landscape.server
      server_version: '19.10'
      server_ppa: "ppa:landscape/19.10"
      server_packages:
        - landscape-server-quickstart
        - landscape-api
```

## License

GPL 3.0

## Author information

Christian Stankowic (info@cstan.io)
