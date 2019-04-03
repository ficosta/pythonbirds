class Pessoa:
    def cumprimentar(self):
        return f'Ol￿á {id(self)}'

if __name__ == '__main__':
    p = Pessoa()
    print(p.cumprimentar())