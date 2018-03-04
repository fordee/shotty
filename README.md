# snapshotalyzer3000

Utility to manage EC2 snapshots. Safely take snapshots of your EC2 instances.

## About

An AWS utility that manages EC2 instances. Groups of instances can be handled together with tag Project tags on your EC2 instances.

## Configuration

shotty uses the configuration file creates by AWS cli e.g.:

`aws configure --profile shotty`

## Running

`pipenv run "python shotty/shotty.py <command> <subcommand> <--project=PROJECT>"`

 - *command* is instance, volumes, or snapshots.
 - *subcommand* depends on command.
 - *project* (optional) is the tag where Name=Project.
