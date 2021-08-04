# htb-api

Some basic scripts to dump and process data from the Hack The Box API.

## Overview

These scripts are mainly used to:

- Identify retired and active machines in the HTB labs
- Process machine data to find machines based on difficulty, release date or platform
- Determine the correct machine naming conventions

The main resouce when creating these scripts was the [Hack The Box v4 API Community Documentation by Propolisa](https://github.com/Propolisa/htb-api-docs). This independent project links to [HTB v4 API Documentation (via Postman)](https://documenter.getpostman.com/view/13129365/TVeqbmeq) - which is awesome to lookup API endpoints to get more information on the Hack The Box API.

## Quickstart

- Download this repo
- `git clone https://github.com/thomaslaurenson/htb-api.git`
- Enter the project folder
- `cd htb-api`
- Add the project folder to your Python PATH
- `export PYTHONPATH=$PYTHONPATH:$(pwd)`
- Create Python virtual environment
- `python3 -m venv venv`
- Activate Python virtual environment
- `source venv/bin/activate`
- Install requirements
- `pip3 install -r requirements.txt`
- Add your HTB email and password to the environment variables file
- `vim .env`
- Run any of the scripts!

## Data

There are some potentially useful JSON files in the `data` folder.

- `machines_target_list.json`: List of HTB machines on the [NetSecFocus Trophy room](https://docs.google.com/spreadsheets/d/1dwSMIAPIam0PuRBkCiDI88pU3yzrqqHkDtBngUHNCw8/htmlview#) list
- `machines_advanced_list.json`: List of **advanced** HTB machines on the [NetSecFocus Trophy room](https://docs.google.com/spreadsheets/d/1dwSMIAPIam0PuRBkCiDI88pU3yzrqqHkDtBngUHNCw8/htmlview#) list
