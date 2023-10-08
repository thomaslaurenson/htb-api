# Update data/machines_*.json files
# This includes active, retired, startingpoint
run_dump_machines:
	python3 -m venv ./venv; \
	. ./venv/bin/activate && \
	pip3 install -r requirements.txt && \
	python3 python/dump_machines.py

# Update data/machines_avatars.json files
run_dump_avatars:
	python3 -m venv ./venv; \
	. ./venv/bin/activate && \
	pip3 install -r requirements.txt && \
	python3 python/dump_avatars.py

run_convert_avatars:
	python3 -m venv ./venv; \
	. ./venv/bin/activate && \
	pip3 install -r requirements.txt && \
	python3 python/convert_avatars_to_png.py

# Generate data for pickthebox web app
run_generate_pickthebox:
	python3 -m venv ./venv; \
	. ./venv/bin/activate && \
	pip3 install -r requirements.txt && \
	python3 python/generate_pickthebox.py

# Generate readme table for trophy room repo
run_generate_readme_table:
	python3 -m venv ./venv; \
	. ./venv/bin/activate && \
	pip3 install -r requirements.txt && \
	python3 python/generate_readme_table.py

# Generate flake8
run_flake8:
	python3 -m venv ./venv; \
	. ./venv/bin/activate && \
	pip3 install -r requirements.txt && \
	python3 -m flake8
