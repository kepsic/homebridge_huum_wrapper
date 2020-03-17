#!/bin/bash

DIR=`dirname "$0"`

cd $DIR
if [ ! -f $DIR/../bin/pserve ]
    then 
    echo "Missing virtual env"
    exit 100
fi

daemon_name=HuumWrapper
if [ ! -d /tmp/updater ]
then
mkdir /tmp/updater
fi

if [ -f /tmp/updater/$daemon_name-remote.lock ] ; then
    exit 100
fi

touch /tmp/updater/$daemon_name-remote.lock



while true
do
$DIR/../bin/pserve $DIR/homebridge_huum_wrapper.ini| tee >/dev/null
done

rm -f /tmp/updater/$daemon_name-remote.lock
