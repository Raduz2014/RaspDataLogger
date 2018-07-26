#! /bin/sh

V1_WEBAPI_LOGS="/home/pi/RaspDataLogger/DataloggerWebApp/WebApi/v1/logs/v1_restapi.log"

if [ $# -eq 0 ]; then
	tail -n 45 $V1_WEBAPI_LOGS
 elif [ $# -eq 1 ]; then
	tail -n $1 $V1_WEBAPI_LOGS
 elif [ $# -eq 2 ]; then
	if [ $1 = "w" && -z "$2" ]; then
		watch -n 2 tail -n 45 $V1_WEBAPI_LOGS
	else
		watch -n 2 tail -n $2 $V1_WEBAPI_LOGS
	fi
fi

