class Programa:
    def __init__(self, nome, ano, ):
        self._nome = nome.title() #definindo como privado
        self.ano = ano
        self._likes = 0 #definindo como privado

    @property # usar property ao inves de usar getter assim todos os lugares que já acessam a classe precisam mudar.
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property # usar property ao inves de usar getter assim todos os lugares que já acessam a classe precisam mudar.
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'Nome: {self.nome} -  {self.ano} - {self.likes} Likes'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} -  {self.ano} - {self.duracao} min - {self.likes} Likes'

        
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} -  {self.ano} - {self.temporadas} temporadas - {self.likes} Likes'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self.programas = programas

    def tamanho(self):
        return len(self.programas)


vingadores = Filme('vigadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2019, 2)
tmep = Filme ('Todo mundo em panico', 1999, 100 )
demolidor = Serie('Demolidor', 2016, 2)

vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()

#print(f'Nome: {atlanta.nome} - {atlanta.ano} -  {atlanta.temporadas} - {atlanta.likes}')
#print("Nome: {} - Ano: {} - Temporadas: {}".format(atlanta.nome, atlanta.ano, atlanta.temporadas)) - outra forma

filmes_e_series = [ vingadores, atlanta, demolidor, tmep ]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

for programa in playlist_fim_de_semana.programas:
    print(programa)
