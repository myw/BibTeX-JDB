#!/bin/sh
#
awk -F= '/Journal =/{ gsub("[{},]", "", $2); sub(" ", "", $2); print $2 }' < $1 | sort -u
