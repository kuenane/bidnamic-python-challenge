#!/usr/bin/env python
# coding: utf-8

# # Import CSV files to a postgres database


#import libraries
#conda install psycopg2
#pip install psycopg2
#pip install python-dotenv

import os
import numpy as np
import pandas as pd
import psycopg2




#main 

from data_files import *
from dotenv import dotenv_values, load_dotenv
load_dotenv()


def main():
    print(dotenv_values(".env") )

#settings
    dataset_dir = 'datasets'

#db settings
    host = os.environ.get("HOST")
    dbname = os.environ.get("DBNAME")
    user = os.environ.get("USER")
    password = os.environ.get("PASSWORD")

#configure environment and create main df
    csv_files_ = csv_files()
    configure_dataset_directory(csv_files_, dataset_dir)
    df = create_df(dataset_dir, csv_files_)

    for k in csv_files_:

#call dataframe
        dataframe = df[k]

#clean table name
        tbl_name = clean_tbl_name(k)
    
#clean column names
        col_str, dataframe.columns = clean_colname(dataframe)
    
#upload data to db   
        upload_to_db(host, 
                 dbname, 
                 user, 
                 password, 
                 tbl_name, 
                 col_str, 
                 file=k, 
                 dataframe=dataframe, 
                 dataframe_columns=dataframe.columns)
if __name__ == "__main__":
    main()

