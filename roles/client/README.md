# client

This role registers [Ubuntu Landscape](https://ubuntu.com/landscape) clients.

## Requirements

No requirements.

## Role Variables

| Variable | Default | Description |
| -------- | ------- | ----------- |
| `client_computer_title` | FQDN | Computer title within Landscape |
| `client_landscape_server` | - | Landscape server to register to |
| `client_landscape_ssl` | `/etc/landscape/landscape_server.pem` | Landscape server SSL public key |
| `client_account_name` | `standalone` | Account name used for registration |
| `client_tags` | - | Optional tags for the client |
| `client_registration_key` | - | Key for registration


## Dependencies

No dependencies.

## Example Playbook

Refer to the following example:

```yaml
- hosts: clients
  roles:
    - role: stdevel.landscape.client
      client_landscape_server: sgiertz.robots.loc
```

Set additional variables if required, e.g.:

```yaml
---
- hosts: my-client
  roles:
    - role: stdevel.landscape.client
      client_landscape_server: gugugaga.pinkepank.loc
      client_computer_title: 'my-client.pokemans.loc'
```

## License

GPL 3.0

## Author Information

Christian Stankowic (info@cstan.io)
