This is a CLI application to parse and display survey data from CSV files, and display the results in an output file.

Prerequisites

Install Python 3
Install Pandas library (pip3 install pandas)
Install Numpy library
Install argparse library
A EC2 instance where launch the scripts or a AWS Lambda

The exercise was probably been designed for Ruby and push data output in Tableau, but I preferred use 
Python because is much performant (in my opinion) for any BI tool, included the possibility to be used in Machine Learning
with iPython notebooks launched by Sagemaker.


The comments are inside the file survey.py and the syntax to be launched is:

python3 survey.py --inputfile survey-1.csv --outputfile output1.txt
python3 survey.py --inputfile survey-2.csv --outputfile output2.txt
python3 survey.py --inputfile survey-3.csv --outputfile output3.txt

There is a bash script that launch the  scripts in realtime is called bound.sh
You can run it continuosly using a cron like:

* * * * * /yourpath/bound.sh >/dev/null 2>&1

The content of bound.sh and the crontab both could be part of a Jenkins job.

Annex a documentation of my feedback system interpretation using realtime data, please read feedback-system.pdf and
the python file cutomer-feedback.py.

Thanks

Tony


 
