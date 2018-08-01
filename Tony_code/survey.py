"""

put what this code does here

"""

import pandas as pd
import numpy as np
import argparse

def read_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputfile", help="input survey questions")
    parser.add_argument("--outputfile", help="output survey results")
    args = parser.parse_args()
    files = []
    if args.inputfile:
        files.append(args.inputfile)
    if args.outputfile:
        files.append(args.outputfile)

    return tuple(files)

def get_results(surveys, survey_questions):
    survey_summary = {}
    submitted_surveys = surveys[surveys['SubmittedAt'].notnull()]
    participation_count = submitted_surveys.shape[0]
    participation_percentage = round((submitted_surveys.shape[0]/surveys.shape[0]) * 100, 2)
    survey_summary['participation_count'] = participation_count
    survey_summary['participation_percentage'] = participation_percentage

    # you need to check if survey_questions dataframe are rating type questions before doing the following

    for column in submitted_surveys.columns[3:]:
        survey_summary[column+"_mean_rating"] = submitted_surveys[column].mean()

    return survey_summary

def write_output(survey_summary, outputfile):
    f = open(outputfile, "w")
    for key, value in survey_summary.items():
        f.write(str(key) + " : " + str(value) + "\n")
    f.close()

if __name__ == '__main__':
    
    print("running....")
    (inputfile, outputfile) = read_args()

    columns_survey1_responses = ['Email'
      , 'EmployeeId'
      , 'SubmittedAt'
      , 'Answer1'
      , 'Answer2'
      , 'Answer3'
      , 'Answer4'
      , 'Answer5']

    columns_survey1 = ['theme'
        , 'type'
        , 'text']
    
    responses = {'survey-1.csv':'survey-1-responses.csv', 'survey-2.csv':'survey-2-responses.csv', 'survey-3.csv':'survey-3-responses.csv' }

    # gets response file name based on survey file name
    filename = responses.get(inputfile)
    print(filename)

    # reads response file name as a pandas dataframe
    survey1_responses_df = pd.read_csv(filename, header=None, sep=',', skip_blank_lines=True,names=columns_survey1_responses)
    survey1_df = pd.read_csv(inputfile, header=None, sep=',', skip_blank_lines=True,names=columns_survey1)

    # gets the required output results
    survey_results = get_results(survey1_responses_df, survey1_df)

    # writes the output to the output file
    write_output(survey_results, outputfile)

