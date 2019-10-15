#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 12:00:09 2019

@author: afonsohsabino
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tmdb = pd.read_csv("tmdb_5000_movies.csv")

tmdb.head()

#Trabalhando com as variáveis do TMDB

tmdb.original_language.unique()

tmdb.original_language.value_counts()

#Transformando a séria em DataFrame

tmdb.original_language.value_counts().to_frame()

#Reset o indice para coluna

#Opção 1 de plotagem de categoria
languageCount = tmdb.original_language.value_counts().to_frame().reset_index()

languageCount.columns = ["Language", "Total"]

languageCount.head()

#Plots de Categoria

sns.barplot(x="Language", y="Total", data=languageCount)

#Opção 2 de plotagem de categoria (outra forma de fazer)
sns.catplot(x = "original_language", kind = "count", data = tmdb)

#Novas formas de visualizar os dados

plt.pie(languageCount.Total, labels = languageCount.Language)

#Separando o Ingles das demais linguas

totalPerLanguage = tmdb.original_language.value_counts()
totalInEnglish = totalPerLanguage.loc["en"]
allTotal = totalPerLanguage.sum()
totalOtherLanguage = allTotal - totalInEnglish

#Criando um DataFrame para visualizar English vs Others

dados = {
    'idioma' : ['ingles', 'outros'],
    'total' : [totalInEnglish, totalOtherLanguage]
}
dados = pd.DataFrame(dados)
dados
sns.barplot(x = "idioma", y = "total", data = dados)

plt.pie(dados['total'], labels = dados['idioma'])

#Analisando os dados dos outros idiomas

totalPerOtherLanguages = tmdb.query("original_language != 'en'").original_language.value_counts()

otherLanguages = tmdb.query("original_language != 'en'")

#Plotagem configurando o aspect ratio, ordem e palheta de cores

sns.catplot(x = 'original_language', 
            kind = 'count', 
            data = otherLanguages, 
            aspect = 2, 
            palette= "BuGn_r", 
            order = totalPerOtherLanguages.index)

#Outros exemplos de plotagem

sns.set(style="ticks")

# Load the example dataset for Anscombe's quartet
df = sns.load_dataset("anscombe")

# Show the results of a linear regression within each dataset
sns.lmplot(x="x", y="y", col="dataset", hue="dataset", data=df,
           col_wrap=2, ci=None, palette="muted", height=4,
           scatter_kws={"s": 50, "alpha": 1})

