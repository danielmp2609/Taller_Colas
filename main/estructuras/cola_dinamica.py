from estructuras.nodo import Nodo

class ColaDinamica:
    def __init__(self):
        self.p = None   
        self.r = None   

    def esta_vacia(self):
        return self.p is None

    def enqueue(self, dato):
        if self.p is None:
            self.p = Nodo(dato)
            self.r = self.p
        else:
            q = Nodo(dato)
            self.r.sig = q
            self.r = q

    def dequeue(self):
        if self.p is None:
            return None
        else:
            dato = self.p.info
            self.p = self.p.sig

            if self.p is None:
                self.r = None
            return dato

    def mostrar(self):
        if self.p is None:
            return "La cola está vacía!!"
        q = self.p
        elementos = []
        while q is not None:
            elementos.append(str(q.info.pid))
            q = q.sig
        return " -> ".join(elementos)