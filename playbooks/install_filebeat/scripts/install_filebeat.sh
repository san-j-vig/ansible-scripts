#!/bin/bash
rm /etc/apt/sources.list.d/elastic-8.x.list -f &> /dev/null
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
apt-get install apt-transport-https -y
echo "deb https://artifacts.elastic.co/packages/8.x/apt stable main" | tee /etc/apt/sources.list.d/elastic-8.x.list
apt-get update && sudo apt-get install filebeat
systemctl enable filebeat
service filebeat start
rm /etc/apt/sources.list.d/elastic-8.x.list -f
