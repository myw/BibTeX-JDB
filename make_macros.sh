#!/bin/bash

usage () {
	echo "$0 -[hfns] <journal abbreviation database>"
	echo -e "\n\tDefaults: .bib-style macro, abbreviated journal name, dots"
	echo -e "\t\te.g. Journal of Physical Chemistry -> J. Chem. Phys."
	echo -e "\n\t-h - print this help message"
	echo -e "\t-f - use the full journal name, not an abbreviation [full]"
	echo -e "\t-n - do not use dots [nodots]"
	echo -e "\t-s - make a .bst-style macro instead [style]"
	exit 1
}

field=2
nodot=0
left='@string{'
middle=' = \"'

while getopts fhns opt; do
	case $opt in
		h)
			usage
			;;
		f)
			field=3
			;;
		n)
			nodot=1
			;;
		s)
			left='MACRO{'
			middle='} {\"'
			;;
	esac

done
shift $(($OPTIND - 1))

if [ -z "$1" ]; then
	usage
else
	awk -v field=$field -v nodot=$nodot -v left="$left" -v middle="$middle" -F'|' '
		{	if (nodot && field == 2){ 
				gsub("\\.", "", $field) 
			}
			print left $1 middle $field "\"}" 
		}
	' $@ | sort -u 
fi
