# htb-api

Some scripts to dump and process data from the Hack The Box (HTB) API.

This project is by no way associated with Hack The Box.

## Overview

This project provides a very basic library to authenticate with HTB and dump machine & machine avatar data - this is found in the `src` folder. Examples of usage is available in the `examples` folder. There is also some data dumped in the `data` folder to ease processing, stored in JSON format.

The main resource when creating these scripts was the [Hack The Box v4 API Community Documentation by Propolisa](https://github.com/Propolisa/htb-api-docs). This independent project links to [HTB v4 API Documentation (via Postman)](https://documenter.getpostman.com/view/13129365/TVeqbmeq) - which is awesome to lookup API endpoints to get more information on the Hack The Box API.

## Project Status

This project is "hacked" together, mainly to fetch some data about machines from Hack The Box. There are no tests and no library deployed to PyPi. I do not envision adding much more to the project, as I do not need any other data (yet!). Feel free to submit a PR, fork and modify, or just grab the `htb.py` file and extend.

If you require a more robust library, I recommend the [`PyHackTheBox` package](https://github.com/clubby789/htb-api) - however, it does not seem to be updated to recent HTB API changes, according to my testing and [this open issue](https://github.com/clubby789/htb-api/issues/62).

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

Add the `htb` directory to `PYTHONPATH` environment variable:

```
export PYTHONPATH="$PYTHONPATH:$(pwd)/htb"
```

- Run any of the scripts in the `examples` folder!
- Deactivate virtual environment when done

```none
deactivate
```
