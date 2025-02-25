br = 'Flamengo', 'Santos', 'Palmeiras', 'Gremio', 'Athletico-PR', 'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goias'
print(f' lista dos 10 primeiros da tabela {br}')
print(f'Os 5 primeiros são {br[:5]}')
print(f'os ultimos  4 ultimos {br[6:]}')
print(f'Os times em ordem alfabetica {sorted(br)}')
print(f'O {br[5]} esta na {br.index("São Paulo") + 1}ª posição')

