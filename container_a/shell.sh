#!/bin/bash

TARGET=/work/source/


inotifywait -m -e create -e moved_to --format "%f" $TARGET \
        | while read FILENAME
                do
                        echo Detected $FILENAME, Checking whether json file  or not
                        if [[ $FILENAME == *.json ]]
                        then

                        echo  I am inside the  now converting json to xml
                        python pyscript.py "$FILENAME"
                        else
                        echo $FILENAME is not a json file
                        fi
                        
                done
