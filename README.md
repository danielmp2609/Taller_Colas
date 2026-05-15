⚙️ Taller 2 - Colas Dinámicas y Planificación de CPU
📌 Descripción del proyecto

Este proyecto fue desarrollado para el Taller 2 de Estructuras de Datos, enfocado en la implementación de una cola dinámica utilizando listas enlazadas, aplicándola en una simulación de planificación de procesos de CPU.

A diferencia de una implementación básica, este proyecto lleva la estructura de datos a un caso práctico real utilizado en sistemas operativos:

Gestión de procesos
Planificación de CPU
Simulación de algoritmos de despacho

El sistema permite registrar procesos manualmente y ejecutarlos mediante dos algoritmos clásicos:

✅ FCFS (First Come First Served)
✅ Round Robin

Todo esto fue desarrollado desde cero usando estructuras dinámicas y una interfaz gráfica amigable en Python.

🎯 Objetivo del taller

Comprender el funcionamiento de las colas dinámicas implementando:

Nodos enlazados
Inserción y eliminación en cola
Manejo de punteros (frente y final)
Aplicación práctica en planificación de CPU
Visualización mediante interfaz gráfica
🧠 Conceptos aplicados
Cola dinámica

La cola trabaja bajo el principio:

FIFO → First In, First Out

El primer proceso que entra es el primero en salir.

Ejemplo:

P1 → P2 → P3

Sale primero: P1
🧩 Estructura implementada
Clase Nodo

Representa cada nodo de la lista enlazada:

class Nodo:

Cada nodo contiene:

información
referencia al siguiente nodo
Clase Proceso

Representa cada proceso de CPU:

class Proceso:

Cada proceso contiene:

ID del proceso
tiempo total de ejecución
tiempo restante (para Round Robin)
Clase ColaDinamica

Implementación manual de la cola utilizando:

p → frente
r → final

Operaciones implementadas:

Encolar (enqueue)

Inserta elementos al final

enqueue()
Desencolar (dequeue)

Elimina elementos del frente

dequeue()
Mostrar cola
mostrar()

Permite visualizar el estado actual de la cola.

⚡ Algoritmo FCFS (First Come First Served)

Este algoritmo ejecuta los procesos en orden de llegada.

Funcionamiento:
Los procesos ingresan a la cola
Se ejecutan completamente
No existe interrupción

Ejemplo:

P1 → P2 → P3

Orden de ejecución:

P1
P2
P3
Métricas calculadas

El sistema calcula automáticamente:

Tiempo de espera
Tiempo de retorno
Promedio de espera
Promedio de retorno
🔄 Algoritmo Round Robin

Simula multitarea usando un quantum.

Cada proceso recibe un tiempo limitado de CPU.

Si no termina:

➡ vuelve al final de la cola

Ejemplo:

Quantum = 2
P1 → P2 → P3

Si P1 no termina:

P2 → P3 → P1

Esto continúa hasta finalizar todos los procesos.

🖥 Interfaz gráfica

Desarrollada completamente con Tkinter

Permite:

✅ Registrar procesos
✅ Asignar tiempo de ejecución
✅ Configurar quantum
✅ Ejecutar FCFS
✅ Ejecutar Round Robin
✅ Visualizar resultados
✅ Limpiar cola de procesos

🎨 Características visuales

Se implementó una interfaz moderna con:

tema oscuro
colores personalizados
botones interactivos
consola de resultados
visualización de cola en tiempo real
📂 Estructura del proyecto
Taller_Colas/
│
├── main.py
├── README.md
🚀 Cómo ejecutar el proyecto

Clonar repositorio:

git clone https://github.com/TU-USUARIO/Taller_Colas.git

Entrar al proyecto:

cd Taller_Colas

Ejecutar:

python main.py
💻 Tecnologías utilizadas
Python 3
Tkinter
Estructuras dinámicas
Listas enlazadas
Git
GitHub
📚 Aprendizajes obtenidos

Durante este proyecto se reforzaron conocimientos sobre:

Colas dinámicas
Nodos enlazados
Planificación de CPU
Algoritmos de scheduling
Interfaces gráficas
Organización lógica del código
🔥 Diferencia frente a una cola básica

Este proyecto no solo implementa una cola tradicional.

También demuestra una aplicación real de la estructura en:

Sistemas operativos → administración de procesos

Lo que lo hace mucho más práctico y cercano a escenarios reales.

👨‍💻 Autor

** - Daniel Esteban Monterroza Pérez** ** - Jose Jose Arcia Jaramillo** ** - Alexis Armando Mendoza Martinez**

Proyecto académico desarrollado para la asignatura de Estructuras de Datos

✅ Conclusión

Este taller demuestra cómo una estructura de datos aparentemente sencilla puede utilizarse para resolver problemas reales.

Se implementó desde cero una cola dinámica con listas enlazadas y se aplicó en algoritmos reales de planificación de CPU, complementado con una interfaz gráfica que facilita su comprensión visual.

No fue solamente implementar una cola. Fue llevar la teoría a una simulación funcional. 🔥
