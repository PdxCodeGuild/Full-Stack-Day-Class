#!/bin/bash

OLD_PREFIX="$1"
NEW_PREFIX="$2"


for FILE in $OLD_PREFIX*
do
    OLD_FILE="$(realpath $FILE)"
    NEW_FILE=$(echo $OLD_FILE | ruby -pe "\$_.gsub!('$OLD_PREFIX', '$NEW_PREFIX')")
    mv -n $OLD_FILE $NEW_FILE
done

ruby -i -pe "\$_.gsub!('$OLD_PREFIX', '$NEW_PREFIX')" *.md **/*.md
