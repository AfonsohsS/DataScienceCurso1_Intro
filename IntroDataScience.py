#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 18:35:42 2019

@author: afonsohsabino
"""
#Analisando as notas dos filmes

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

notas = pd.read_csv("ratings.csv")

notas.columns = ["UsuarioId", "filmeId", "nota", "data"]

notas.head()

notas.nota.value_counts()

mean = notas.nota.mean()

#Plotando histograma das notas

notas.nota.plot(kind='hist')

median = notas.nota.median()

print("Média:", mean)
print("Mediana:", median)

notas.nota.describe()

#Utilizando um exemplo do Seaborn

sns.boxplot(notas.nota)

notas.nota.unique()

#Carregando os filmes e vendo suas notas

movies = pd.read_csv("movies.csv")

movies.columns = ["filmeId", "titulo", "generos"]

movies.head()

notas.query('filmeId==1').nota.value_counts()

notas.query('filmeId==1').nota.mean()

media_por_filme = notas.groupby('filmeId').mean().nota

media_por_filme.head()

media_por_filme.plot(kind="hist")

sns.boxplot(media_por_filme)

sns.distplot(media_por_filme, bins=10)

#Plot sem biblioteca... Uso em mais baixo nível

plt.hist(media_por_filme)
plt.title("Histograma das médias dos filmes")

notas.nota.describe()

