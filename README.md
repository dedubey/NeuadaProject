# NeuadaProject
Task Details and Requirements

The Project contains the following folders and files:
1.	container_a
2.	container_b
3.	source
4.	shared
5.	destination 
6.	docker-compose.yml
 container_a folder contains the following files:
1.	dockerfile   ---- to build the docker image for container A
2.	shell.sh       ----  to keep a watch on source folder ( as soon as a new json file is detected     
                            pyscript.py will be run )
3.	pyscript.py  --- python script to convert json to xml then encrypt it and send it to the shared
                           folder
4.	requirements.txt   ---- list of dependency to be installed by container A. this will be used by 
                                      dockerfile
container_b folder contains the following files:
1.	dockerfile   ---- to build the docker image for container B
2.	shell.sh       ----  to keep a watch on shared folder ( as soon as a new encrypted file is detected     
                            pydec.py will be run )
3.	pyscript.py  --- python script to decrypt the xml then and store it in the destination 
                            folder
4.	requirements.txt   ---- list of dependency to be installed by container B. this will be used by 
                                      dockerfile

To run the project on a machine , docker and docker-compose should be installed and running on the machine.  To run the project, just run following command 

docker-compose up 

NOTE: All the files and folders names and relative location shouldn’t be changed.  To run the project , navigate to the ubuntu folder given and run docker-compose up. 
The rest of the files were used for testing and they are not required in the project. 





The source folder is mounted on container A.
The destination folder is mounted to Container B. 
The shared folder is mounted to both the Containers. Consider shared folder as a network shared drive which is accessible from both the Containers. 

Flow chart can be seen in files. 

 
