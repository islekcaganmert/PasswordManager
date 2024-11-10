
# PasswordManager

An *experimental* password manager based on [TheProtocols](https://theprotocols.islekcaganmert.me/)
![demo](https://raw.githubusercontent.com/islekcaganmert/PasswordManager/refs/heads/main/tests/screenshot.png)[![TheProtocols](https://img.shields.io/badge/TheProtocols-Synced-green
)](https://theprotocols.islekcaganmert.me/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


## Features

- Cloud Sync using TheProtocols
- Encrypted vault
- Single-click complete data removal
- Simple terminal-based UI
## Installation

```bash
git clone https://github.com/islekcaganmert/PasswordManager.git
cd PasswordManager
pymake restore
```
    
## Usage

```bash
pymake test main
```


## Tech Stack

**Client:** [Python](https://python.org), [TheProtocols.py](https://pypi.org/project/TheProtocols/), AES

**Cloud Storage:** [TheProtocols](https://theprotocols.islekcaganmert.me/)
## FAQ

#### Why should we prefer this?

There is two types of password managers: cloud ones and local ones. If you use cloud saved one, your control on your own data is limited. If you use local one, your passwords will be inaccessible on your other devices. Thanks to TheProtocols, we can solve this problem. This password manager is based on an open protocol that lets users to inspect all of their data saved into app data registry.

#### If registry is inspectable, can't other apps read passwords?

Yes and no. This **experimental** implementation matches vault password with account password which means every app which knows account password with `InterApp` permission can read passwords. If these two passwords are different, no app can access without vault password as a symmetric encryption is used.

#### When this will be available in non-experimental way?

Soon. You can follow HereUS PBC on [X](https://x.com/hereus_pbc), [Bluesky](https://bsky.app/profile/hereus.net) or fediverse using [Bridgy Fed](https://fed.brid.gy).
## Feedback

If you have any feedback, please [email](mailto:islekcaganmert@gmail.com) me.

