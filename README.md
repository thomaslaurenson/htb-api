# htb-api

Some scripts to dump and process data from the Hack The Box (HTB) API.

## Overview

These scripts are mainly used to:

- Identify retired and active machines in the HTB labs
- Process machine data to find machines based on difficulty, release date or platform
- Determine the correct machine naming conventions

The main resource when creating these scripts was the [Hack The Box v4 API Community Documentation by Propolisa](https://github.com/Propolisa/htb-api-docs). This independent project links to [HTB v4 API Documentation (via Postman)](https://documenter.getpostman.com/view/13129365/TVeqbmeq) - which is awesome to lookup API endpoints to get more information on the Hack The Box API.

## Quickstart

- Download this repo, and enter folder.

```none
git clone https://github.com/thomaslaurenson/htb-api.git && cd htb-api
```

- Create Python virtual environment, activate it, and install requirements.

```none
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

- Add your HTB email and password to the environment variables file

```none
vim .env
```

- Run any of the scripts in the `python` folder!
- Deactivate virtual environment when done

```none
deactivate
```

## Data

There are some potentially useful JSON files in the `data` folder.

- `machines_oscp_list.json`: List of HTB machines on the [NetSecFocus Trophy room](https://docs.google.com/spreadsheets/d/1dwSMIAPIam0PuRBkCiDI88pU3yzrqqHkDtBngUHNCw8/htmlview#) list
- `machines_oscp_advanced_list.json`: List of **advanced** HTB machines on the [NetSecFocus Trophy room](https://docs.google.com/spreadsheets/d/1dwSMIAPIam0PuRBkCiDI88pU3yzrqqHkDtBngUHNCw8/htmlview#) list
