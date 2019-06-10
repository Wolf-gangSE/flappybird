import pyxel
import random

# DIRECIONAMENTO DO PASSARO
CIMA = 0
BAIXO = 1

# MODOS DE JOGO
INICIO = 0
RODANDO = 1
GAME_OVER = 3

class Platforms:
    def __init__(self, FPS=30):
        self.plataformas = []
        self.x_borda1 = 231
        self.x_base1 = 235
        self.y_base1 = random.randint(0, 160)
        self.y_borda1 = self.y_base1
        self.x_borda2 = 231
        self.x_base2 = 235
        self.y_borda2 = self.y_borda1 + 60
        self.y_base2 = self.y_borda2 + 8
        self.distancia_base1 = self.y_base1
        self.distancia_base2 = pyxel.height - self.y_base2

        pyxel.load('Bird.pyxel')

    def update(self):
        self.x_base1 = self.x_base1 - 1
        self.x_base2 = self.x_base2 - 1
        self.x_borda1 = self.x_borda1 - 1
        self.x_borda2 = self.x_borda2 - 1

        self.nova_borda1 = (self.x_borda1, self.y_borda1)
        self.plataformas.append(self.nova_borda1)
        self.nova_base2 = (self.x_base2, self.y_base2)
        self.plataformas.append(self.nova_base2)
        self.nova_base1 = (self.x_base1, self.y_base1)
        self.plataformas.append(self.nova_base1)
        self.nova_borda2 = (self.x_borda2, self.y_borda2)
        self.plataformas.append(self.nova_borda2)


    def draw(self):
        pyxel.blt(self.nova_borda1[0], self.nova_borda1[1], 0, 12, 64, 24, 8)
        pyxel.blt(self.nova_borda2[0], self.nova_borda2[1], 0, 12, 64, 24, 8)
        pyxel.blt(self.nova_base1[0], 0, 0, 64, 0, 16, self.distancia_base1)
        pyxel.blt(self.nova_base2[0], self.nova_base2[1], 0, 64, 0, 16, self.distancia_base2)


class Bird:
    def __init__(self):
        self.bird = (50, 100)
        self.direcao = BAIXO
        pyxel.load('Bird.pyxel')

    def update(self):
        if pyxel.frame_count % 6 == 0:
            # movimenta de acordo com entrada do usuario
            if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
                self.direcao = CIMA
            else:
                self.direcao = BAIXO

        cabeca= self.bird

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
        self.plataforms = Platforms()
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
        self.passaro.draw()
        pyxel.blt(pyxel.mouse_x, pyxel.mouse_y, 0, 0, 16, 16, 16, 1)

    def nova_plataforma(self):
        if self.modo_jogo == RODANDO:
            self.plataforms.update()
            self.plataforms.draw()


Jogo()