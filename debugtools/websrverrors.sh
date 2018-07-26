#!/bin/sh
APACHE_ERR="/var/log/apache2/error.log"

if [ $# -eq 0 ]; then
	tail -n 45 $APACHE_ERR
 elif [ $# -eq 1 ]; then
	tail -n $1 $APACHE_ERR
 elif [ $# -eq 2 ]; then
	if [ $1 = "w" && -z "$2" ]; then
		watch -n 2 tail -n 45 $APACHE_ERR
	else
		watch -n 2 tail -n $2 $APACHE_ERR
	fi
fi
