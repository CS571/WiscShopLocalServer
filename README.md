## Basic usage

### About

A local endpoint for the WiscShop server provided as an alternative to the endpoint available at https://mysqlcs639.cs.wisc.edu

### Environment setup



Install conda, the run the following commands:


#### Linux 
````
conda env create --file linux_requirements.txt --name server_env
````

#### Windows 10 
````
conda env create --file windows_requirements.txt --name server_env
````

to create the conda environment, then 

````
conda activate server_env
````

to activate the conda environment. When this enviroment is activated, you should be able to run the server as specified below. 



### To Start Endpoint
````
python3 ./api.py
````

