#!/bin/bash

# Check if an argument is passed
if [ -z "$1" ]; then
  echo "Error: No version bump type provided. Please use 'patch', 'minor', or 'major'."
  exit 1
fi

# Ensure the argument is one of patch, minor, or major
if [[ "$1" != "patch" && "$1" != "minor" && "$1" != "major" ]]; then
  echo "Error: Invalid version bump type '$1'. Please use 'patch', 'minor', or 'major'."
  exit 1
fi

# Bump the version using the provided argument
bump-my-version bump $1

echo "Version bumped and pushed to GitHub."