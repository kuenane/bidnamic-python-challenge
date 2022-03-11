# A RESTful API in Flask using SQLAlchemy
The idea: A simple RESTful API created using Flask and SQLAlchemy that interacts with a PostgreSQL database of doctors and reviews.

Python Version Used: Python 3.6.0

### Installation:

0) Ensure that python is installed version by checking version. To check, run `python3 -V`. If you do not have it, you can install it 
1) Clone the Github repo: `$ git clone https://github.com/kuenane/bidnamic-python-challenge`
2) Move into the project directory `$ cd flask-restapi`
3) Setup a virtual environment in the project folder
4) Start the virtual environment. You should see `(venv)` in as part of the command prompt once it is started.
*NOTE*: To stop the virtual environment at any time, run `(venv) $ deactivate`
5) Install all the requirements, including flask. Be sure not to use `sudo` as this will install flask in the global environment instead of the virtual environment: `(venv) $ pip install -r requirements.txt`
6) In a separate terminal window, install PostgreSQL. 
7) After PostgreSQL is setup
8) In a separate terminal window, run `$ psql`. Then, run relevant checks to see if tables are created
9) Finally, run `# \q` to quit psql, 

### To Run:


0) Run `python main.py` to populate and create the databases
1) Set an export path for flask: `(venv) $ export FLASK_APP=app.py or (venv) $ set export FLASK_APP=app.py`
2) Run flask! `(venv) $ flask run`
3) Go to http://127.0.0.1:5000 in a browser


# API Documentation

**Show Search_Term**
----
  Returns json data about a single search iterm.

* **URL**

  /api/v1/search_term/:id

* **Method:**

  `GET`

*  **URL Params**

   **Required:**

   `id=[integer]`

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    
    **Delete, Update and Patch methods to be implemented**

* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{"error": "Search_term does not exist"}`

**Create Search_term**
----
  Search_term returning top 10 search_terms by ROAS and returns json data 

* **URL**

  /api/v1/search_term

* **Method:**

  `POST`

*  **URL Params**

   None

* **Data Params**

  

* **Success Response:**

  * **Code:** 201 <br />
   

* **Error Response:**

  * **Code:** 400 BAD REQUEST <br />
    **Content:** `{"error": "Missing required data."}`

**Show Alias**
----
  Returns json data about a single alias.

* **URL**

  /api/v1/alias/:id

* **Method:**

  `GET`

*  **URL Params**

   **Required:**

   `id=[integer]`

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
   
`

* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{"error": "Alias does not exist."}`

**Create alias**
----
  Creates a alias and returns json data about that Review

* **URL**

  /api/v1/alias

* **Method:**

  `POST`

*  **URL Params**

   None

* **Data Params**


* **Success Response:**

  * **Code:** 201 <br />
    
* **Error Response:**

  * **Code:** 400 BAD REQUEST <br />
    **Content:** `{"error": "Missing required data."}`

    OR

  * **Code:** 400 UNAUTHORIZED <br />
    **Content:** `{ error : "Given item does not exist." }`

