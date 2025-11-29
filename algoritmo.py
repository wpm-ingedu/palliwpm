import random
class Juego:
    armado,sudo,nivel=[],[],0
    def __init__(self,nivel):
        self.nivel=nivel
        self.crear()
        self.ordenado()
        self.barajea()
        self.transpuesta()
        self.barajea()
        self.transpuesta()
        self.barajea()
        self.elJuego()    
    def crear(self):
        lista=[1,2,3,4,5,6,7,8,9]
        random.shuffle(lista)
        for i in range(9):
                fila=[]
                for j in range(9):
                    fila.append(lista[j-i])
                self.armado.append(fila)
    def ordenado(self):
        a=[self.armado[0],self.armado[3],self.armado[6]]
        b=[self.armado[1],self.armado[4],self.armado[7]]
        c=[self.armado[2],self.armado[5],self.armado[8]]
        self.armado=[]
        self.armado.extend(a)
        self.armado.extend(b)
        self.armado.extend(c)
    def transpuesta(self):
        nuevo=[]
        for i in range(len(self.armado[1])):
            fila=[]
            for j in range(len(self.armado)):
                fila.append(self.armado[j][i])
            nuevo.append(fila)
        self.armado=[]
        self.armado=nuevo
        
    def barajea(self):
        a=[self.armado[0],self.armado[1],self.armado[2]]
        b=[self.armado[3],self.armado[4],self.armado[5]]
        c=[self.armado[6],self.armado[7],self.armado[8]]
        random.shuffle(a)
        random.shuffle(b)
        random.shuffle(c)
        self.armado=[]
        self.armado.extend(a)
        self.armado.extend(b)
        self.armado.extend(c)
    def elJuego(self):
        self.sudo=[]
        dificultad=[[0,0,0,0,1,1,1,1,1,1],[0,0,0,0,0,1,1,1,1,1],[0,0,0,0,0,0,1,1,1,1],[0,0,0,0,0,0,0,1,1,1],[0,0,0,0,0,0,0,0,1,1]]    
        for i in range(9):
            fila=[]
            for j in range(9):
                azar= random.randint(0,9)
                if dificultad[self.nivel][azar]==1:
                    fila.append(self.armado[i][j])
                else:
                    fila.append(0)
            self.sudo.append(fila) 
    

    