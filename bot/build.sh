#!/usr/bin/env bash

echo "just a dummy bot/build.sh script that logs SLURM environment settings..."

env | grep SLURM_

echo "also log CUSTOM_ vars"

env | grep CUSTOM_
