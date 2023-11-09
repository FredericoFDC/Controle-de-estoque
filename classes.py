class Nome():
    def __init__(self, nome, sobrenome, segundo_nome):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__segundo_nome = segundo_nome

    def primeiro_nome(self):
        print(f"Seu primeiro nome é {self.__nome} e seu sobrenome é {self.__sobrenome} seu nome nome completo é {self.__nome} {self.__sobrenome} {self.__segundo_nome}")

frederico = Nome('Frederico', 'Ferrarezi', 'Costa')
frederico.primeiro_nome()
jhow = Nome('Jhonatan', 'Teixeira', 'Dultra Primeiro')
jhow.primeiro_nome()
