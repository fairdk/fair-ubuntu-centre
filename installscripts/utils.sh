#!/bin/bash

# Easily make a replacement and escape the input and output strings
function sedeasy {
  sed -i "s/$(echo $1 | sed -e 's/\([[\/.*]\|\]\)/\\&/g')/$(echo $2 | sed -e 's/[\/&]/\\&/g')/g" $3
}

# Delete a line containing $1 in file $2
function sedeasy_delete {
  sed -i "/$(echo $1 | sed -e 's/\([[\/.*]\|\]\)/\\&/g')/d" $2
}
