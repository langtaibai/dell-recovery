#!/bin/sh

. /usr/share/dell/scripts/fifuncs ""

export DEBIAN_FRONTEND=noninteractive

IFHALT "Install dell-recovery recommends"
apt-get install --yes --allow-unauthenticated cd-boot-images-amd64 || true
apt-get install --yes --allow-unauthenticated wodim || true
apt-get install --yes --allow-unauthenticated xorriso || true
IFHALT "Done with dell-recovery recommends"
