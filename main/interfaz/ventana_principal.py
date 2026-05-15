import tkinter as tk
from tkinter import scrolledtext

from estructuras.proceso import Proceso

from algoritmos.fcfs import fcfs
from algoritmos.round_robin import round_robin


class AppColas:
    def __init__(self, root):
        self.root = root
        self.root.title("Taller 2 – Colas Dinámicas | Planificación de CPU")
        self.root.geometry("820x720")
        self.root.configure(bg="#1a1a2e")
        self.root.resizable(True, True)

        self.lista_procesos = []
        self._build_ui()

    def _build_ui(self):
        # ---- TÍTULO ----
        titulo_frame = tk.Frame(self.root, bg="#16213e", pady=12)
        titulo_frame.pack(fill="x")

        tk.Label(
            titulo_frame,
            text="COLAS DINÁMICAS",
            font=("Courier New", 22, "bold"),
            fg="#e94560",
            bg="#16213e"
        ).pack()
        tk.Label(
            titulo_frame,
            text="Planificación de CPU  ·  FCFS  y  Round Robin  ·  Lista Enlazada",
            font=("Courier New", 10),
            fg="#a8b2d8",
            bg="#16213e"
        ).pack()

        # ---- REGISTRO DE PROCESOS ----
        reg_frame = tk.Frame(self.root, bg="#1a1a2e", pady=8, padx=20)
        reg_frame.pack(fill="x")

        tk.Label(
            reg_frame,
            text="Registrar proceso:",
            font=("Courier New", 11, "bold"),
            fg="#ccd6f6",
            bg="#1a1a2e"
        ).grid(row=0, column=0, columnspan=4, sticky="w", pady=(0, 4))

        # ID
        tk.Label(reg_frame, text="ID:", font=("Courier New", 10), fg="#a8b2d8", bg="#1a1a2e").grid(row=1, column=0, sticky="w")
        self.entry_pid = tk.Entry(
            reg_frame, font=("Courier New", 12), bg="#0f3460", fg="#e2e8f0",
            insertbackground="#e94560", relief="flat", bd=0,
            highlightthickness=2, highlightcolor="#e94560", highlightbackground="#334155", width=10
        )
        self.entry_pid.grid(row=1, column=1, ipady=6, padx=(4, 16))

        # Tiempo
        tk.Label(reg_frame, text="Tiempo:", font=("Courier New", 10), fg="#a8b2d8", bg="#1a1a2e").grid(row=1, column=2, sticky="w")
        self.entry_tiempo = tk.Entry(
            reg_frame, font=("Courier New", 12), bg="#0f3460", fg="#e2e8f0",
            insertbackground="#e94560", relief="flat", bd=0,
            highlightthickness=2, highlightcolor="#e94560", highlightbackground="#334155", width=10
        )
        self.entry_tiempo.grid(row=1, column=3, ipady=6, padx=(4, 16))
        self.entry_tiempo.bind("<Return>", lambda e: self.agregar_proceso())

        # Botón agregar
        tk.Button(
            reg_frame, text="+ Agregar",
            command=self.agregar_proceso,
            font=("Courier New", 10, "bold"),
            bg="#e94560", fg="white",
            activebackground="#c73652", activeforeground="white",
            relief="flat", padx=10, pady=5, cursor="hand2"
        ).grid(row=1, column=4, padx=(0, 8))

        # Botón limpiar procesos
        tk.Button(
            reg_frame, text="Limpiar lista",
            command=self.limpiar_procesos,
            font=("Courier New", 10, "bold"),
            bg="#334155", fg="white",
            activebackground="#e94560", activeforeground="white",
            relief="flat", padx=10, pady=5, cursor="hand2"
        ).grid(row=1, column=5)

        # ---- LISTA DE PROCESOS ENCOLADOS ----
        cola_frame = tk.Frame(self.root, bg="#1a1a2e", padx=20)
        cola_frame.pack(fill="x")

        tk.Label(
            cola_frame,
            text="Cola de procesos (frente → final):",
            font=("Courier New", 10),
            fg="#64748b",
            bg="#1a1a2e"
        ).pack(anchor="w")

        self.lbl_cola = tk.Label(
            cola_frame,
            text="[ vacía ]",
            font=("Courier New", 12, "bold"),
            fg="#4ade80",
            bg="#0d1117",
            anchor="w",
            padx=8, pady=6
        )
        self.lbl_cola.pack(fill="x", pady=(2, 6))

        # ---- CONFIGURACIÓN Y BOTONES ----
        ctrl_frame = tk.Frame(self.root, bg="#1a1a2e", padx=20, pady=4)
        ctrl_frame.pack(fill="x")

        tk.Label(ctrl_frame, text="Quantum (RR):", font=("Courier New", 10), fg="#a8b2d8", bg="#1a1a2e").pack(side="left")
        self.entry_quantum = tk.Entry(
            ctrl_frame, font=("Courier New", 12), bg="#0f3460", fg="#e2e8f0",
            insertbackground="#e94560", relief="flat", bd=0,
            highlightthickness=2, highlightcolor="#e94560", highlightbackground="#334155", width=6
        )
        self.entry_quantum.insert(0, "2")
        self.entry_quantum.pack(side="left", ipady=6, padx=(4, 20))

        botones = [
            ("▶ FCFS",        "#0f3460", self.ejecutar_fcfs),
            ("▶ Round Robin", "#1a472a", self.ejecutar_rr),
            ("Limpiar",       "#334155", self.limpiar_resultado),
        ]
        for texto, color, cmd in botones:
            tk.Button(
                ctrl_frame, text=texto, command=cmd,
                font=("Courier New", 10, "bold"),
                bg=color, fg="white",
                activebackground="#e94560", activeforeground="white",
                relief="flat", padx=12, pady=6, cursor="hand2"
            ).pack(side="left", padx=(0, 8))

        # ---- ÁREA DE RESULTADOS ----
        result_frame = tk.Frame(self.root, bg="#1a1a2e", padx=20)
        result_frame.pack(fill="both", expand=True, pady=(4, 4))

        tk.Label(
            result_frame,
            text="Resultados:",
            font=("Courier New", 11, "bold"),
            fg="#ccd6f6",
            bg="#1a1a2e"
        ).pack(anchor="w")

        self.text_resultado = scrolledtext.ScrolledText(
            result_frame,
            font=("Courier New", 12),
            bg="#0d1117", fg="#58a6ff",
            insertbackground="white",
            relief="flat", bd=0,
            highlightthickness=1,
            highlightcolor="#334155",
            highlightbackground="#21262d",
            wrap="word", state="disabled"
        )
        self.text_resultado.pack(fill="both", expand=True, pady=(4, 0))

        self.text_resultado.tag_configure("titulo",    foreground="#e94560", font=("Courier New", 12, "bold"))
        self.text_resultado.tag_configure("resultado", foreground="#4ade80", font=("Courier New", 13, "bold"))
        self.text_resultado.tag_configure("paso",      foreground="#a8b2d8", font=("Courier New", 11))
        self.text_resultado.tag_configure("error",     foreground="#f97316", font=("Courier New", 11, "bold"))
        self.text_resultado.tag_configure("info",      foreground="#7dd3fc", font=("Courier New", 11))
        self.text_resultado.tag_configure("sep",       foreground="#334155", font=("Courier New", 11))

        # ---- PIE ----
        tk.Label(
            self.root,
            text="Estructuras de Datos  ·  Cola Dinámica con Lista Enlazada (Clase Nodo)  ·  Python",
            font=("Courier New", 8),
            fg="#334155",
            bg="#1a1a2e"
        ).pack(pady=(0, 6))

    # ---- HELPERS ----
    def _escribir(self, texto, tag=""):
        self.text_resultado.config(state="normal")
        self.text_resultado.insert("end", texto + "\n", tag)
        self.text_resultado.config(state="disabled")
        self.text_resultado.see("end")

    def _limpiar_resultado(self):
        self.text_resultado.config(state="normal")
        self.text_resultado.delete("1.0", "end")
        self.text_resultado.config(state="disabled")

    def _actualizar_lbl_cola(self):
        if not self.lista_procesos:
            self.lbl_cola.config(text="[ vacía ]")
        else:
            partes = [f"{p.pid}({p.tiempo})" for p in self.lista_procesos]
            self.lbl_cola.config(text="  →  ".join(partes))

    # ---- AGREGAR PROCESO ----
    def agregar_proceso(self):
        pid = self.entry_pid.get().strip()
        tiempo_str = self.entry_tiempo.get().strip()

        if not pid:
            self._limpiar_resultado()
            self._escribir("ERROR: El ID del proceso no puede estar vacío.", "error")
            return
        if any(p.pid == pid for p in self.lista_procesos):
            self._limpiar_resultado()
            self._escribir(f"ERROR: Ya existe un proceso con ID '{pid}'.", "error")
            return
        try:
            tiempo = int(tiempo_str)
            if tiempo <= 0:
                raise ValueError
        except ValueError:
            self._limpiar_resultado()
            self._escribir("ERROR: El tiempo debe ser un número entero positivo.", "error")
            return

        proc = Proceso(pid, tiempo)
        self.lista_procesos.append(proc)
        self._actualizar_lbl_cola()
        self.entry_pid.delete(0, "end")
        self.entry_tiempo.delete(0, "end")
        self.entry_pid.focus()

        self._limpiar_resultado()
        self._escribir(f"Proceso '{pid}' con tiempo {tiempo} agregado a la cola.", "info")

    # ---- EJECUTAR FCFS ----
    def ejecutar_fcfs(self):
        if not self.lista_procesos:
            self._limpiar_resultado()
            self._escribir("ERROR: La cola está vacía. Agrega procesos primero.", "error")
            return

        self._limpiar_resultado()
        self._escribir("ALGORITMO: FCFS (First Come, First Served)", "titulo")
        self._escribir("Orden de llegada → orden de ejecución (sin interrupciones)", "info")
        self._escribir("─" * 48, "sep")

        pasos = fcfs(self.lista_procesos)
        for tag, texto in pasos:
            self._escribir(texto, tag)

    # ---- EJECUTAR ROUND ROBIN ----
    def ejecutar_rr(self):
        if not self.lista_procesos:
            self._limpiar_resultado()
            self._escribir("ERROR: La cola está vacía. Agrega procesos primero.", "error")
            return

        try:
            quantum = int(self.entry_quantum.get().strip())
            if quantum <= 0:
                raise ValueError
        except ValueError:
            self._limpiar_resultado()
            self._escribir("ERROR: El quantum debe ser un número entero positivo.", "error")
            return

        self._limpiar_resultado()
        self._escribir("ALGORITMO: ROUND ROBIN", "titulo")
        self._escribir("Cada proceso se ejecuta por turnos según el quantum.", "info")
        self._escribir("─" * 48, "sep")

        pasos = round_robin(self.lista_procesos, quantum)
        for tag, texto in pasos:
            self._escribir(texto, tag)

    # ---- LIMPIAR PROCESOS ----
    def limpiar_procesos(self):
        self.lista_procesos = []
        self._actualizar_lbl_cola()
        self._limpiar_resultado()
        self._escribir("Lista de procesos limpiada. Puedes agregar nuevos procesos.", "info")

    def limpiar_resultado(self):
        self._limpiar_resultado()