#!/bin/bash

# Helper script for creating deployments using gitflow when
# hosting on Github

# Assumes that gitflow is being followed, as documented here
# https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow/

# Branches:
#  - master: contains tagged versions of the released code
#  - release-ma.mi-pa: one branch per release, one of this may currently be validated
#  - develop: contains the code currently in development

# This script fits into the part where 

# Relevant APIs:
# Fetch tag: https://api.github.com/repos/molmed/chiasma/tags?access_token=

