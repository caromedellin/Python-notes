My first Notebook on Data with Python
===============
I will be exploring [pandas](http://pandas.pydata.org/), since it's the one I have been recommended for quite some time now. I am choosing this over R mainly because I do not require the data visualization part that it gives you. I intend to do the data visualization part later with D3.js. In any case, this will document my experiences learning Python.
### I also found this amazing resource 
[Pandas cookbook](https://github.com/jvns/pandas-cookbook)

##API reference that concerns me
[Pandas API](http://pandas.pydata.org/pandas-docs/stable/api.html)
###JSON
```python
read_json([path_or_buf, orient, typ, dtype, ...]) #Convert a JSON string to pandas object
json_normalize(data[, record_path, meta, ...])  #“Normalize” semi-structured JSON data into a flat table
```
###HTML
```python
read_html(io[, match, flavor, header, ...]) #Read HTML tables into a list of DataFrame objects.
```
###STATA
```python
read_stata(filepath_or_buffer[, ...]) #Read Stata file into DataFrame
StataReader.data(**kwargs) #DEPRECATED: Reads observations from Stata file, converting them into a dataframe
StataReader.data_label()  # Returns data label of Stata file
StataReader.value_labels() # Returns a dict, associating each variable name a dict, associating
StataReader.variable_labels() # Returns variable labels as a dict, associating each variable name
StataWriter.write_file()
```

Installing Relevant Software
============================
For Officially Python 2.7, 3.4, and 3.5, for some reason everyone warns against using Python 3, Do not use Python 3!


###Guide of this Repo:
Section | Description
--- | ---
[Introduction to Python]('python-intro/basics.md') | Cheat sheet of Python commands and short descriptions.
