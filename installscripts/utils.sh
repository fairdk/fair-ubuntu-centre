#!/bin/bash

# Delete a line containing $1 in file $2
function sedeasy_delete {
  sed -i "/$(echo $1 | sed -e 's/\([[\/.*]\|\]\)/\\&/g')/d" $2
}
