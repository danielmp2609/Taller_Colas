from estructuras.cola_dinamica import ColaDinamica
from estructuras.proceso import Proceso

def fcfs(procesos):
    cola = ColaDinamica()
    pasos = []
    tiempo_actual = 0
    metricas = []

    for proc in procesos:
        p_copia = Proceso(proc.pid, proc.tiempo)
        cola.enqueue(p_copia)

    pasos.append(("info", f"Cola inicial: {cola.mostrar()}"))
    pasos.append(("sep", "─" * 48))

    while not cola.esta_vacia():
        proceso = cola.dequeue()
        inicio = tiempo_actual
        fin = tiempo_actual + proceso.tiempo
        espera = inicio
        retorno = fin

        pasos.append(("titulo", f"Ejecutando: {proceso.pid}"))
        pasos.append(("paso",   f"  Inicio: t={inicio}  |  Fin: t={fin}  |  Duración: {proceso.tiempo}"))
        pasos.append(("paso",   f"  Tiempo de espera: {espera}  |  Tiempo de retorno: {retorno}"))

        tiempo_actual = fin
        metricas.append((proceso.pid, proceso.tiempo, espera, retorno))

    prom_espera  = sum(m[2] for m in metricas) / len(metricas)
    prom_retorno = sum(m[3] for m in metricas) / len(metricas)

    pasos.append(("sep", "─" * 48))
    pasos.append(("titulo", "RESUMEN FCFS"))
    pasos.append(("paso", f"  {'Proceso':<12} {'Duración':<12} {'Espera':<12} {'Retorno':<12}"))
    pasos.append(("paso", f"  {'─'*9:<12} {'─'*8:<12} {'─'*6:<12} {'─'*7:<12}"))
    for pid, dur, esp, ret in metricas:
        pasos.append(("paso", f"  {pid:<12} {dur:<12} {esp:<12} {ret:<12}"))
    pasos.append(("resultado", f"  Promedio espera:   {prom_espera:.2f}"))
    pasos.append(("resultado", f"  Promedio retorno:  {prom_retorno:.2f}"))

    return pasos