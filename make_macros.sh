#!/bin/bash

field=2
nodot=0
left='MACRO{'
middle='} {\"'

while getopts fns opt; do
	case $opt in
		f)
			field=3
			;;
		n)
			nodot=1
			;;
		s)
			left='@string{'
			middle=' = \"'
			;;
	esac

done
shift $(($OPTIND - 1))

awk -v field=$field -v nodot=$nodot -v left="$left" -v middle="$middle" -F'|' '
	{	if (nodot && field == 2){ 
			gsub("\\.", "", $field) 
		}
		print left $1 middle $field "\"}" 
	}
' $@ | sort -u 
