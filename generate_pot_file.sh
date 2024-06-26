#!/bin/bash

# generate a .pot file
(find ./all_pages -name "*.py" -print0; find . -name "common_config.py" -print0) | xargs -0 xgettext -o ./locales/base.pot
