### To Run:

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

