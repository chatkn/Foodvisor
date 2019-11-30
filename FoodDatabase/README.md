# FoodDatabase

Database able to continuously maximize coverage and granularity of existing labeled data.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Prerequisites

You need to install Python3 and insert the database.py module path in your *PYTHONPATH* variable on your environment.

After cloning this repository, you must to find in the FoodDatabase folder:
- a **main.py** file corresponding to the executable of the program.
- a **database.py** file which is the module imported.
- a **test_samples** folder, containing 3 tests folders to test the project.

## Running the tests

To run the program easily without changing the source code, you will find a tests_samples folder containing 3 others folders.
In each folder, there are 3 files :
- a **graph_build** file that init the graph
- a **img_extract** file describing the images label to extract. 
- a **graph_edits** file that describe the new nodes to add in the graph

To import others test, you must to create another test folder in *FoodDatabase/tests_samples/* containing 3 files:
- a file to init the graph
- a file describing the extract images.
- a file that describe the additionnal node to add in the graph

See the initials tests folders as examples.

The Usage to run the program is as follows:
```
python main.py -b <buildGraphFile> -x <extractImageFile> -e <editedGraphFile>
```
Example:
```
python main.py -b test_samples/test1/graph_build1.json -x test_samples/test1/img_extract1.json -e test_samples/test1/graph_edits1.json 
```

