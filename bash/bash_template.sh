#!/bin/bash
#
# template_script.sh
#


program="template_script.sh"

function usage() {
    cat <<EOF
$program, SHORT DESCRIPTION

Usage: $program [OPTIONS] POSITIONAL_ARGUMENTS

$program LONG DESCRIPTION

$program accepts the following options:

    -q
        Quiet mode. Only output warnings and errors.
    -d
        Enable debug mode.
    -h
        Show usage help.
EOF
}

# Set-up colours for message printing if we're not piping and terminal is
# capable of outputting the colors.
_color_terminal=$(tput colors 2>&1)
if [[ -t 1 ]] && (( ${_color_terminal} > 0 )); then
    _text_bold=$(tput bold)
    _text_white=$(tput setaf 7)
    _text_blue=$(tput setaf 6)
    _text_green=$(tput setaf 2)
    _text_yellow=$(tput setaf 3)
    _text_red=$(tput setaf 1)
    _text_reset=$(tput sgr0)
else
    _text_bold=""
    _text_white=""
    _text_blue=""
    _text_green=""
    _text_yellow=""
    _text_red=""
    _text_reset=""
fi

# Set-up functions for printing coloured messages.
function debug() {
    if [[ $debug != 0 ]]; then
        echo "${_text_bold}${_text_blue}[DEBUG]${_text_reset}" "$@"
    fi
}

function info() {
    if [[ $quiet == 0 ]]; then
        echo "${_text_bold}${_text_white}[INFO] ${_text_reset}" "$@"
	fi
}

function success() {
    if [[ $quiet == 0 ]]; then
        echo "${_text_bold}${_text_green}[OK]   ${_text_reset}" "$@"
    fi
}

function warning() {
    echo "${_text_bold}${_text_yellow}[WARN] ${_text_reset}" "$@"
}

function error() {
    echo "${_text_bold}${_text_red}[ERROR]${_text_reset}" "$@" >&2
}

# Define error codes.
SUCCESS=0
ERROR_ARGUMENTS=1

# Disable debug and quiet modes by default.
debug=0
quiet=0

# If no arguments were given, just show usage help.
if [[ -z $1 ]]; then
    usage
    exit "$SUCCESS"
fi

# Parse the arguments
while getopts "qdh" opt; do
    case "$opt" in
	q) quiet=1;;
	d) debug=1;;
        h) usage
           exit "$SUCCESS";;
        *) usage
           exit "$ERROR_ARGUMENTS";;
    esac
done
i=$OPTIND
shift $(($i-1))