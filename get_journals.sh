#!/bin/sh
#

usage () {
	echo "$0 <.bib file> - get a list of all the journal names in a .bib file"
	exit 1
}


if [ -z "$1" ]; then
	usage
else
	awk -F= '/Journal =/{ gsub("[{},]", "", $2); sub(" ", "", $2); print $2 }' < $1 | sort -u
fi

