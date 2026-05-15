from estructuras.cola_dinamica import ColaDinamica
from estructuras.proceso import Proceso

def round_robin(procesos, quantum):

    cola = ColaDinamica()
    pasos = []
    tiempo_actual = 0
    llegada = {}     
    fin_tiempo = {}    
    tiempos = {}      

    # Encolar todos los procesos
    for proc in procesos:
        p_copia = Proceso(proc.pid, proc.tiempo)
        cola.enqueue(p_copia)
        llegada[proc.pid] = 0
        tiempos[proc.pid] = proc.tiempo

    pasos.append(("info", f"Cola inicial: {cola.mostrar()}"))
    pasos.append(("info", f"Quantum: {quantum}"))
    pasos.append(("sep", "─" * 48))

    turno = 1

    while not cola.esta_vacia():
        proceso = cola.dequeue()

        ejecutar = min(proceso.restante, quantum)
        inicio = tiempo_actual
        fin = tiempo_actual + ejecutar
        proceso.restante -= ejecutar
        tiempo_actual = fin

        pasos.append(("titulo", f"Turno {turno}: {proceso.pid}"))
        pasos.append(("paso",   f"  Inicio: t={inicio}  |  Fin: t={fin}  |  Ejecutado: {ejecutar}  |  Restante: {proceso.restante}"))

        if proceso.restante > 0:
            cola.enqueue(proceso)
            pasos.append(("paso", f"  → Re-encolado. Cola: {cola.mostrar()}"))
        else:
            fin_tiempo[proceso.pid] = fin
            pasos.append(("paso", f"  ✓ Proceso {proceso.pid} terminado en t={fin}"))

        turno += 1

    pasos.append(("sep", "─" * 48))
    pasos.append(("titulo", "RESUMEN ROUND ROBIN"))
    pasos.append(("paso", f"  {'Proceso':<12} {'Duración':<12} {'Espera':<12} {'Retorno':<12}"))
    pasos.append(("paso", f"  {'─'*9:<12} {'─'*8:<12} {'─'*6:<12} {'─'*7:<12}"))

    metricas = []
    for proc in procesos:
        pid = proc.pid
        dur = tiempos[pid]
        ret = fin_tiempo.get(pid, 0) - llegada[pid]
        esp = ret - dur
        metricas.append((pid, dur, esp, ret))
        pasos.append(("paso", f"  {pid:<12} {dur:<12} {esp:<12} {ret:<12}"))

    prom_espera  = sum(m[2] for m in metricas) / len(metricas)
    prom_retorno = sum(m[3] for m in metricas) / len(metricas)
    pasos.append(("resultado", f"  Promedio espera:   {prom_espera:.2f}"))
    pasos.append(("resultado", f"  Promedio retorno:  {prom_retorno:.2f}"))

    return pasos