import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

filmes = pd.read_csv("movies.csv")
notas = pd.read_csv("ratings.csv")

filmes.columns = ["filmeId", "titulo", "generos"]
notas.columns = ["usuarioId", "filmeId", "nota", "momento"]

filmes.head(2)
notas.head()

notasToyStory = notas.query("filmeId==1")
notasJumanji = notas.query("filmeId==2")

#Use o len() para contar o número de ocorrências
print(len(notasToyStory), len(notasJumanji))

#Imprimindo a média  e mediana das notas com interpolação de 2 casas decimais
print("Média das notas no Toy Story: %.2f" % notasToyStory.nota.mean())
print("Média das notas no Jumanji: %.2f" % notasJumanji.nota.mean())
print("Mediana das notas no Toy Story: %.2f" % notasToyStory.nota.median())
print("Mediana das notas no Jumanji: %.2f" % notasJumanji.nota.median())

#Utilizando o NumPy para criar um array de valores
import numpy as np

filme1 = np.append(np.array([2.5] * 10), np.array([3.5] * 10))
filme2 = np.append(np.array([5] * 10), np.array([1] * 10))

#Extraindo a média e mediana
print(filme1.mean(), filme2.mean())
print(np.median(filme1), np.median(filme2))

#Visualizando a distribuição dos valores com Seaborn
sns.distplot(filme1)
sns.distplot(filme2)

#Visualizando a distribuição dos valores com Matplotlib
plt.hist(filme1)
plt.hist(filme2)

plt.boxplot([notasToyStory.nota, notasJumanji.nota])
