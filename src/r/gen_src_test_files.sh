#!/bin/sh
rm -rf ./tmp
python gen_data_files.py --csv_master ./datasets.csv \
  --src_template ./templates/template.tpl \
  --src_path ./tmp/observations/r \
  --test_template ./templates/test_template.tpl \
  --test_path ./tmp/tests/r \
  --init_template ./templates/init_template.tpl \
  --init_path ./tmp/observations/r
touch ./tmp/tests/__init__.py
touch ./tmp/tests/r/__init__.py
