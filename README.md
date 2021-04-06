# Django-Polls
Polls application using Django

## Table of Content

* [Development Environment Configuration](#development-environment-configuration)
* [Docker](#docker)
* [Built With](#built-with)
* [Authors](#authors)

## Development Environment Configuration

- Download the files from this repository.

    ```bash
  git clone git@github.com:Derhks/Django-Polls.git
  ```

- Create a virtual environment with Anaconda

    ```bash
  conda create -n polls python=3.8 -y
  ```
  
- Now, let's activate the created virtual environment

    ```bash
  conda activate polls
  ```

- Move to the folder derhks_polls

    ```bash
  cd derhks_polls/
  ```

- With the virtual environment activated we are going to install 
  the requirements used in the project

    ```bash
  pip3 install -r requirements.txt
  ```

- The application has its unit tests, run the following command:

    ```bash
  python manage.py test polls
  ```

- Within the requirements we have the Coverage.py tool that allows 
  us to measure the coverage of the app code, execute the command:
  
    ```bash
  coverage run --source='.' manage.py test polls
  ```
  
- We can view the report with the command:
  
    ```bash
  coverage report
  ```
  
- For a nicer presentation use

    ```bash
  coverage html
  ```
  to get annotated HTML listings detailing missed lines.


- To view the html file run the command:

    ```bash
  xdg-open htmlcov/index.html
  ```

- Finally, run the application server

    ```bash
  python manage.py runserver
  ```
  
- After finishing the above steps you can test the application in 
  the browser using the following URL:

    ```bash
  http://127.0.0.1:8000/admin/
  ```


# Configuration in PyCharm to run the server from the top of the IDE

- Press the "Add Configuration..." icon at the top right.

- Click on the plus icon at the top left.

- In the drop-down select "Django Server". 

- In the upper part in the box "Name:" we write the name that we want to give to the server, for example the name of the project.

- In the lower part press the "Apply" and "OK" buttons to save the configuration.

Now you will see that an icon appears with the name you wrote in the "Name:" box, now you can press the "Play" button to run the application server and you can access it from the browser with the URL above.


## Docker
With the help of Docker we can run and test the application with a 
single command


  ```bash
  docker-compose up
  ```
It is necessary to be inside the first directory derhks_polls/ to execute 
the above command


## Built With

- [Python](https://www.python.org/) - Programming language
- [SQLite](https://www.sqlite.org/index.html) - Database
- [HTML](https://www.w3schools.com/html/) - Markup language
- [CSS](https://www.w3schools.com/css/) - Style language
- [Django](https://www.djangoproject.com) - Web framework 

## Authors
- **Julián Sandoval [derhks]** https://github.com/Derhks
