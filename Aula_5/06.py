pessoa = {
    'Nomes': ['Maria', 'Pedro', 'Joao'],
    'ColunaA': [1, 0.5, 3.2],
    'ColunaB': [5, 3, 1]
}

print(pessoa['Nomes'][1], pessoa['ColunaB'][1])

# deve ter um jeito melhor

pessoa2 = {
    'Maria': {
        'ColunaA': 1,
        'ColunaB': 5
    },
    'Pedro':{
        'ColunaA': 0.5,
        'ColunaB': 3
    }
}


print('Pedro: ' ,pessoa2['Pedro']['ColunaB'])