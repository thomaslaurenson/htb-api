create_venv:
	python3 -m venv ./venv; \
	. ./venv/bin/activate && \
	pip3 install -r requirements.txt

get_token:
	export PYTHONPATH="${PYTHONPATH}:$$(pwd)/src" && \
	. ./venv/bin/activate && \
	python3 examples/get_token.py

dump_active_machines:
	export PYTHONPATH="${PYTHONPATH}:$$(pwd)/src" && \
	. ./venv/bin/activate && \
	python3 examples/dump_active_machines.py

dump_retired_machines:
	export PYTHONPATH="${PYTHONPATH}:$$(pwd)/src" && \
	. ./venv/bin/activate && \
	python3 examples/dump_retired_machines.py

dump_avatars:
	export PYTHONPATH="${PYTHONPATH}:$$(pwd)/src" && \
	. ./venv/bin/activate && \
	python3 examples/dump_avatars.py

list_active_machines:
	. ./venv/bin/activate && \
	python3 examples/list_active_machines.py

list_by_release_date:
	. ./venv/bin/activate && \
	python3 examples/list_by_release_date.py

list_trophyroom_machines:
	. ./venv/bin/activate && \
	python3 examples/list_trophyroom_machines.py

generate_pickthebox:
	. ./venv/bin/activate && \
	python3 examples/generate_pickthebox.py

flake8:
	. ./venv/bin/activate && \
	python3 -m flake8 .
