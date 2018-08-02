This is a CLI application to parse and display survey data from CSV files, and display the results in an output file.

Prerequisites

Install Python 
Installl Pandas library
Install Numpy library
Install argparse library

The exercise is probably it has been designed for Ruby and push data output in Tableau, but I preferred use 
Python because is much performant (in my opinion) for any BI tool, included the possibility to be used in Machine Learning
with iPython notebooks launched by Sagemaker.

The next step it should be (my advice) is put everything in a AWS Datapipeline and populate any BI tools like Tableau
R-Server or Kibana (ELK) .

The comments are inside the file survey.py and the syntax to be launched is:

python3 survey.py --inputfile survey-1.csv --outputfile output1.txt
python3 survey.py --inputfile survey-2.csv --outputfile output2.txt
python3 survey.py --inputfile survey-3.csv --outputfile output3.txt

All the files could be used in a bash script and executed in interval wait of 10 seconds depending by the amount of data.

