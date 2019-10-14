#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 12:13:30 2019

@author: afonsohsabino
"""

import pandas as pd
#import seaborn as sns

movies = pd.read_csv("movies.csv")

movies.columns = ["filmeId", "titulo", "generos"]

movies.head()

notas.query('filmeId==1').nota.value_counts()
