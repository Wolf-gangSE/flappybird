import pyxel
import random

# DIRECIONAMENTO DO PASSARO
CIMA = 0
BAIXO = 1

# MODOS DE JOGO
INICIO = 0
RODANDO = 1
GAME_OVER = 3

class Plataforma:
    def __init__(self):
        self.x_borda1 = 231
        self.x_base1 = 235
        self.y_base1 = random.randint(0, 130)
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

    def draw(self):
        pyxel.blt(self.x_borda1, self.y_borda1, 0, 12, 64, 24, 8)
        pyxel.blt(self.x_borda2, self.y_borda2, 0, 12, 64, 24, 8)
        pyxel.blt(self.x_base1, 0, 0, 64, 0, 16, self.distancia_base1)
        pyxel.blt(self.x_base2, self.y_base2, 0, 64, 0, 16, self.distancia_base2)


class Bird:
    def __init__(self, aceleracao):
        self.bird = (50, 100)
        self.direcao = BAIXO
        self.velocidade_y = 0
        self.aceleracao = aceleracao
        self.click = True
        self.impulso = False
        pyxel.load('Bird.pyxel')

    def update(self):
        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON) and self.click:
            self.impulso = True
            self.click = False

        if pyxel.btnr(pyxel.MOUSE_LEFT_BUTTON):
            self.click = True
            self.direcao = BAIXO

        if self.impulso:
            self.direcao = CIMA
            self.velocidade_y = -3
            self.impulso = False

        self.velocidade_y += self.aceleracao
        self.bird = (self.bird[0], self.bird[1] + self.velocidade_y)

    def draw(self):
        if self.direcao == CIMA:
            pyxel.blt(self.bird[0], self.bird[1], 0, 0, 80, 16, 16, 15)
        else:
            pyxel.blt(self.bird[0], self.bird[1], 0, 0, 0, 16, 16, 15)


class Jogo:
    def __init__(self):
        pyxel.init(255, 200, fps=60)
        pyxel.load('Bird.pyxel')
        self.plataformas = []
        self.passaro = Bird(0.2)
        self.modo_jogo = INICIO
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.modo_jogo == INICIO:
            if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
                self.modo_jogo = RODANDO
        if self.modo_jogo == RODANDO:
            self.passaro.update()
            for p in self.plataformas:
                p.update()
            if pyxel.frame_count % 180 == 0:
                self.nova_plataforma()
        if self.modo_jogo == GAME_OVER:
            pass

    def nova_plataforma(self):
        plataforma = Plataforma()
        self.plataformas.append(plataforma)

    def draw(self):
        pyxel.cls(12)
        if self.modo_jogo == INICIO:
            pyxel.text(100, 60, 'Flappy Bird', 0)
            pyxel.text(90, 140, 'Toque para comecar', 6)
        if self.modo_jogo == RODANDO:
            for p in self.plataformas:
                p.draw()
        self.passaro.draw()
        pyxel.blt(pyxel.mouse_x, pyxel.mouse_y, 0, 0, 16, 16, 16, 1)

Jogo()
