#!/bin/bash
for P in {1..3} ; do python survey.py --inputfile survey-${P} --outputfile output${P}.txt ; done
