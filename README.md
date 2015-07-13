# Project 1: logfind

## Projects The Hard Way

http://projectsthehardway.com/2015/06/16/project-1-logfind-2/

(Command Line, Python)

LogFind scans log files without the user having to explicitly declare every
file on the command line.

## Usage

Logs files are specified in ~/.logfind as a list of paths (regular expressions
allowed).

    logfind [-o] string [string ...]

    string      Search string to find in log files.
    -o          OR logic used instead (AND used by default)

