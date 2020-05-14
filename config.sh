#!/bin/bash

# install package
pip install --upgrade git-annex-remote-globus

# authenticate in Globus.org
git-annex-remote-globus setup


# enable globus remote
git annex enableremote globus
