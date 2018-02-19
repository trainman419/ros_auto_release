#!/usr/bin/env python
#
# Automatic Release script for ROS packages
#
# Author: Austin Hendrix
# Copyright Austin Hendrix, 2018

from __future__ import print_function

"""
Automatic release script for ROS packages released with bloom

This script is designed to be run from a cron job, and it will automatically
increment the version number, update changelogs and do a bloom release of each
package for each distribution, if that package has changed since the previous
release.

Config file format:
The config file describes which packages to release, and which ROS
distributions to release for.

The config file format is a map from package name to list of ROS distros to
release to.

{
    "pacckage1": [ "distro1", "distro2" ],
    "pacckage2": [ "distro2" ],
}

State file format:
The state file describes the state of each package, and is used to determine
if a new release needs to be prepared for each package.

The state file format is a map from package name to maps from ros distro to
most recently released git SHA

{
    "package1": { "distro1": "sha", "distro2": "sha" }
    "package2": { "distro2": "sha" }
}
"""

import argparse
import yaml
import sys

CONFIG_NAME = "ros_auto_release_config.yaml"
STATE_NAME  =  "ros_auto_release_state.yaml"

def load_config():
    with open(CONFIG_NAME, "r") as config:
        return yaml.load(config)

def load_state():
    with open(STATE_NAME, "r") as state:
        return yaml.load(state)

def write_state(state):
    with open(STATE_NAME, "w") as state_out:
        yaml.dump(state, state_out, default_flow_style=False)

def main():
    parser = argparse.ArgumentParser()

    args = parser.parse_args()

    config = load_config()
    if config is None:
        print("ERROR: config is empty!")
        sys.exit(1)

    for package, distros in config.iteritems():
        # Clone the package (or go to a cached checkout and do a pull)
        for distro in distros:
            # Get the branch from bloom
            # Check out the branch
            # Check if the branch has been updated
            # If the branch has changes since last release:
                # Run catkin_generate_changelog
                # Run catkin_prepare_release
                # Commit and push
                # Run bloom-release package --track distro
                # ( assumes distro and track names are the same )
            pass

if __name__ == '__main__':
    main()
