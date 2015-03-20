#!/bin/bash

SOURCE_PATH=$( cd "$PWD/${BASH_SOURCE[0]%/*}"; pwd )
cd "$SOURCE_PATH/.."

# Get the user input:
read -p "Username: " ttiUsername
read -p "Gameserver (DEFAULT:  167.114.28.238): " TTI_GAMESERVER
TTI_GAMESERVER=${TTI_GAMESERVER:-"167.114.28.238"}

# Export the environment variables:
export ttiUsername=$ttiUsername
export ttiPassword="password"
export TTI_PLAYCOOKIE=$ttiUsername
export TTI_GAMESERVER=$TTI_GAMESERVER

echo "==============================="
echo "Starting Toontown Fellowship"
echo "Username: $ttiUsername"
echo "Gameserver: $TTI_GAMESERVER"
echo "==============================="

if [[ "$OSTYPE" == "darwin"* ]]; then
  export DYLD_LIBRARY_PATH=`pwd`/Libraries.bundle
  export DYLD_FRAMEWORK_PATH="Frameworks"

  ppython -m toontown.toonbase.ClientStart
else
  /usr/bin/python2 -m toontown.toonbase.ClientStart
fi
