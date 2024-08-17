#!/bin/bash

# 安装新包
pip install "$1"

# 更新 requirements.txt
# pipreqs . --force
pipreqs ./xfree --force