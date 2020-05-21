#!/bin/bash

TARGET=/work/shared/


inotifywait -m -e create -e moved_to --format "%f" $TARGET \
        | while read FILENAME
                do
                        echo Detected $FILENAME, Checking whether  end  enc
                        if [[ $FILENAME == *.enc ]]
                        then

                        echo   Decrypting the file 
                        python pydec.py "$FILENAME"
                        else
                        echo $FILENAME is not  encrypted 
                        fi

                done
