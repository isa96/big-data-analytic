# Big Data Analysis 

### mtsamples.csv
Medical transcript data taken from [mtsamples](https://www.mtsamples.com). The data consists of 5003 records and 5 columns, namely:
* Type/Specialty: Disease Type / Field
* Sample Name: Sample name
* Description: A brief description of the transcript sample
* Transcript: Transcript details
* Keywords: Related keywords

### mtsamples_scraping.ipynb
Notebook for scraping the web [mtsamples](https://www.mtsamples.com).
Scraping uses the Python programming language and the [Beautiful Soup] library (https://beautiful-soup-4.readthedocs.io/en/latest/#)

### mapper.py & reducer.py
Python script to perform the mapReduce process on text.
