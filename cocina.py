from abc import ABC, abstractmethod

class PedidoBase(ABC):
    @abstractmethod
    def crear_pedido(self):
        pass

class Cliente:
    def __init__(self, nombre):  
        self.nombre = nombre

    def realizar_pedido(self, detalle):
        print(f"{self.nombre} está realizando un pedido.")
        pedido = Pedido(detalle)
        pedido.crear_pedido()
        return pedido

    def reingresar_datos(self):
        print(f"{self.nombre} está reingresando los datos del pedido.")

class Pedido(PedidoBase):
    def __init__(self, detalle):  
        self.id_pedido = id(self)
        self.detalle = detalle
        self.estado = "Pendiente"

    def crear_pedido(self):
        print(f"Pedido creado con detalle: {self.detalle} y estado: {self.estado}")

    def emitir_comprobante(self):
        print(f"Comprobante emitido para el pedido ID {self.id_pedido}.")

class ControlPedidos:
    def gestionar_pedido(self, pedido):
        try:
            if not isinstance(pedido, Pedido):
                raise TypeError("El objeto no es un pedido válido.")
            print("ControlPedidos: Gestionando el pedido...")
            pedido.emitir_comprobante()
            return Cocina().preparar_plato(pedido)
        except Exception as e:
            print(f"Error al gestionar el pedido: {e}")

class Cocina:
    def preparar_plato(self, pedido):
        print(f"Cocina: Preparando el plato para el pedido ID {pedido.id_pedido}.")
        pedido.estado = "Preparado"
        print(f"Pedido ID {pedido.id_pedido} ahora está '{pedido.estado}'.")

def main():
    try:
        
        cliente = Cliente("Juan")
        pedido = cliente.realizar_pedido("Pizza Pepperoni")

        
        control = ControlPedidos()
        control.gestionar_pedido(pedido)

    except Exception as e:
        print(f"Error general: {e}")

if __name__ == "__main__": 
    main()
