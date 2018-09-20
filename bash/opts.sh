#!/bin/bash

function usage {
    echo -e "Usage: ./opts.sh -f f_var -e e_var [-n DEFAULT_VALUE]\n"
    exit 1
}


DEFAULT_VALUE='false'

while [[ $# -gt 0 ]]
do
key="$1"

case $key in
    -h|--help)
    usage
    exit 0
    shift
    shift
    ;;
    -f|--fun_var)
    FUN_VAR="$2"
    shift
    shift
    ;;
    -e|--easy_var)
    EASY_VAR="$2"
    shift
    shift
    ;;
    -n|--nuf_flag)
    DEFAULT_VALUE='true'
    shift
    ;;
    *)
    usage
    exit 0
    shift
    ;;
esac
done
