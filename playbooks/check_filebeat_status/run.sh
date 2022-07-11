#!/bin/bash

playbook_yaml_file="playbook.yml"
read -p "Enter hosts file path: " hosts
if [[ -z $hosts ]]; then
    printf "Please enter a valid hosts file path"
else
    printf "Using host file: $hosts"
    ansible-playbook $playbook_yaml_file -i $hosts
fi
printf "Execution Complete"
