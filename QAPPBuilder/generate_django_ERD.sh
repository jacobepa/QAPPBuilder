#!/bin/bash

# --------------------------
# Generate Django ERD v3
# 02/24/2024
# --------------------------
# v3 JS Updated the trim spaces subroutine.

# Get the current date and time
mydate=$(date +"%Y-%m-%d")
mytime=$(date +"%H%M")

# Trim leading/trailing spaces (not needed as date command doesn't add them)
DateStr="${mydate}_${mytime}"

echo "Writing models for $mydate $mytime"
echo "File name will be $DateStr"

# Specify which models to exclude from the ERD (Django default models)
Exclude=User,Session,AbstractUser,ContentType,Permission,LogEntry,AbstractBaseSession,Group
Include=

# Ensure required Python packages are installed
# pip install graphviz pydotplus

# Generate the ERD with included models
python manage.py graph_models -a -g -I "$Include" -o "../database/models_${DateStr}.png"
python manage.py graph_models -a -g -I "$Include" > "../database/models_${DateStr}.dot"

echo "ERD generation complete."
