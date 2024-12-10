#!/bin/sh

UID=${LOCAL_UID:-1000}
GID=${LOCAL_GID:-1000}

echo "Starting with UID: $UID, GID: $GID"

groupmod -g $GID rustuser
usermod -u $UID -g $GID rustuser

/bin/sh