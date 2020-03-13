import pandas

tabela = pandas.read_csv('alunos.csv')

# print(tabela)
df = pandas.DataFrame(tabela)

# atributos false, true do pandas mudam bastante;

for index, linha in df.iterrows():
    print(index, linha['Nome'])

# aluno2 = open('alunos2.csv', 'a')

# for index, linha in df.iterrows():
#     texto = ()
#     aluno2.write (linha['Nome'])

# aluno2.close()

# df.to_csv('alunos2t.csv', index=False)

# print(df['Nome'])



