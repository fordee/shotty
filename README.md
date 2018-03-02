# snapshotalyzer3000

Utility to manage EC2 instances

## About

An AWS utility that manages EC2 instances.

## Configuration

shotty uses the configuration file creates by AWS cli e.g.:

`aws configure --profile shotty`

## Running

`pipenv run "python shotty/shotty.py <command> <--project=PROJECT>"`

*command* is list, start, stop, or terminate.
*project* (optional) is the tag where Name=Project.
