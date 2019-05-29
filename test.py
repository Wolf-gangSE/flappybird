import pyxel

#DIRECIONAMENTO DO PASSARO
CIMA = 0
BAIXO = 1
DIREITA = 2

#MODOS DE JOGO
INICIO = 0
RODANDO = 1
GAME_OVER = 3

class Platforms:
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass


class Bird:
    def __init__(self):
        self.bird = (50, 100)
        self.direcao = BAIXO
        self.movimento = DIREITA
        pyxel.load('Bird.pyxel')

    def update(self):
        if pyxel.frame_count % 6 == 0:
            # movimenta de acordo com entrada do usuario
            if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
                self.direcao = CIMA
            else:
                self.direcao = BAIXO

        cabeca= self.bird

        if self.movimento == DIREITA:
            cabeca = (cabeca[0] + 1, cabeca[1])

        if self.direcao == CIMA:
            cabeca = (cabeca[0], cabeca[1] - 2)
        elif self.direcao == BAIXO:
            cabeca = (cabeca[0], cabeca[1] + 2)

        self.bird = cabeca

    def draw(self):
        if self.direcao == CIMA:
            pyxel.blt(self.bird[0], self.bird[1], 0, 0, 80, 16, 16, 15)
        else:
            pyxel.blt(self.bird[0], self.bird[1], 0, 0, 0, 16, 16, 15)


class Jogo:
    def __init__(self):
        pyxel.init(255, 200)
        pyxel.load('Bird.pyxel')
        self.passaro = Bird()
        self.modo_jogo = INICIO
        pyxel.run(self.update, self.draw)


    def update(self):
        if self.modo_jogo == INICIO:
            if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
                self.modo_jogo = RODANDO
        if self.modo_jogo == RODANDO:
            self.passaro.update()

    def draw(self):
        pyxel.cls(12)
        if self.modo_jogo == INICIO:
            pyxel.text(100, 60, 'Flappy Bird', 0)
            pyxel.text(90, 140, 'Toque para comecar', 6)
        if self.modo_jogo == RODANDO:
            pyxel.blt(223, 0, 1, 0, 0, 32, 200, 12)
        self.passaro.draw()
        pyxel.blt(pyxel.mouse_x, pyxel.mouse_y, 0, 0, 16, 16, 16, 1)
Jogo()
