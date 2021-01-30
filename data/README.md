## Data sources
This directory contains all the supported data sources. For a data source to be supported it needs to support the following interface:

- to\_json() returns a json version of the data. 
- to\_html() returns an html version of the data.
- get() collectes the data for the current date
- save() saves the data into the database

As each data source will have its own table to manage its data, it needs only get the db connection object so that it can do its own calls to the db

The Data source is expected to get its credentials passed to it when initialized.
