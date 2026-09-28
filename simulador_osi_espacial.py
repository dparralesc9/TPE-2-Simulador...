import tkinter as tk
from tkinter import messagebox
import time
import random
import base64


class SimuladorOSI_Alineado:

    def __init__(self, root):
        self.root = root
        self.root.title("SISTEMA DE COMUNICACIÓN DE DATOS - UNEMI 2026")
        self.root.geometry("1200x850")

        # =========================================================
        # PALETA "ESPACIO PROFUNDO"
        # =========================================================
        self.COLOR_FONDO = "#050414"       # negro-azulado profundo
        self.COLOR_PANEL = "#0b0a24"       # panel ligeramente más claro
        self.COLOR_ACENTO = "#8a5cf6"      # púrpura nebulosa
        self.COLOR_ACENTO2 = "#00e5ff"     # cian estelar (capa activa)
        self.COLOR_EXITO = "#39ff88"       # verde aurora (capa completada)
        self.COLOR_TEXTO = "#e6e6fa"       # lavanda claro
        self.COLOR_TITULO = "#ffd166"      # dorado tipo "estrella"

        self.root.configure(bg=self.COLOR_FONDO)

        # =========================================================
        # FRANJA DE ESTRELLAS (decorativa) DETRÁS DEL ENCABEZADO
        # =========================================================

        self.canvas_estrellas = tk.Canvas(
            root,
            width=1200,
            height=70,
            bg=self.COLOR_FONDO,
            highlightthickness=0
        )

        self.canvas_estrellas.place(x=0, y=0)

        self._dibujar_estrellas(self.canvas_estrellas, 1200, 70, 90)

        # =========================================================
        # ENCABEZADO
        # =========================================================

        tk.Label(
            root,
            text="✦ UNIVERSIDAD ESTATAL DE MILAGRO ✦",
            font=("Helvetica", 18, "bold"),
            bg=self.COLOR_FONDO,
            fg=self.COLOR_TITULO
        ).pack(pady=5)

        tk.Label(
            root,
            text="Simulador OSI — Misión de Comunicación de Datos",
            font=("Helvetica", 10, "italic"),
            bg=self.COLOR_FONDO,
            fg=self.COLOR_ACENTO2
        ).pack()

        # =========================================================
        # NOTA TÉCNICA
        # =========================================================

        self.info_frame = tk.Frame(
            root,
            bg=self.COLOR_PANEL,
            bd=1,
            relief=tk.SOLID,
            highlightbackground=self.COLOR_ACENTO,
            highlightthickness=1
        )

        self.info_frame.pack(
            fill=tk.X,
            padx=40,
            pady=5
        )

        info_text = (
            "NOTA TÉCNICA: El modelo OSI se recorre desde la capa 7 "
            "hasta la capa 1 en el emisor. En el receptor se realiza "
            "el proceso inverso, desde la capa 1 hasta la capa 7."
        )

        tk.Label(
            self.info_frame,
            text=info_text,
            wraplength=1000,
            font=("Arial", 9, "italic"),
            bg=self.COLOR_PANEL,
            fg=self.COLOR_TEXTO
        ).pack(pady=5)

        # =========================================================
        # PANEL DE CONTROL
        # =========================================================

        self.panel = tk.Frame(
            root,
            bg=self.COLOR_FONDO
        )

        self.panel.pack(pady=10)

        self.entrada = tk.Entry(
            self.panel,
            width=40,
            font=("Arial", 11),
            bg=self.COLOR_PANEL,
            fg=self.COLOR_TEXTO,
            insertbackground=self.COLOR_TEXTO
        )

        self.entrada.insert(
            0,
            "Datos de Evaluación UNEMI"
        )

        self.entrada.pack(
            side=tk.LEFT,
            padx=10
        )

        tk.Button(
            self.panel,
            text="🚀 ENVIAR",
            command=self.transmitir,
            bg=self.COLOR_ACENTO,
            fg="white",
            width=12,
            font=("Arial", 10, "bold"),
            activebackground=self.COLOR_ACENTO2
        ).pack(
            side=tk.LEFT,
            padx=5
        )

        tk.Button(
            self.panel,
            text="RESET",
            command=self.resetear,
            bg="#3a3a5c",
            fg="white",
            width=12,
            font=("Arial", 10, "bold"),
            activebackground="#55558a"
        ).pack(
            side=tk.LEFT,
            padx=5
        )

        # =========================================================
        # CONTENEDOR PRINCIPAL
        # =========================================================

        self.main_container = tk.Frame(
            root,
            bg=self.COLOR_FONDO
        )

        self.main_container.pack(
            fill=tk.BOTH,
            expand=True,
            padx=20
        )

        self.main_container.columnconfigure(
            0,
            weight=1
        )

        self.main_container.columnconfigure(
            1,
            weight=0
        )

        self.main_container.columnconfigure(
            2,
            weight=1
        )

        # =========================================================
        # PC-A
        # =========================================================

        self.frame_pca = tk.Frame(
            self.main_container,
            bg=self.COLOR_FONDO
        )

        self.frame_pca.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self.canvas_a = tk.Canvas(
            self.frame_pca,
            width=480,
            height=120,
            bg=self.COLOR_PANEL,
            highlightthickness=1,
            highlightbackground=self.COLOR_ACENTO
        )

        self.canvas_a.pack(pady=5)

        tk.Label(
            self.frame_pca,
            text="🛰 TERMINAL EMISOR - ENCAPSULAMIENTO",
            bg=self.COLOR_FONDO,
            fg=self.COLOR_TITULO,
            font=("Arial", 9, "bold")
        ).pack()

        self.consola_a = tk.Text(
            self.frame_pca,
            width=60,
            height=22,
            bg="#000010",
            fg="#39ff88",
            font=("Consolas", 9),
            insertbackground="#39ff88"
        )

        self.consola_a.pack(pady=5)

        # =========================================================
        # CANAL
        # =========================================================

        self.frame_canal = tk.Frame(
            self.main_container,
            bg=self.COLOR_FONDO
        )

        self.frame_canal.grid(
            row=0,
            column=1,
            padx=10
        )

        self.canvas_canal = tk.Canvas(
            self.frame_canal,
            width=100,
            height=120,
            bg=self.COLOR_FONDO,
            highlightthickness=0
        )

        self.canvas_canal.pack()

        self._dibujar_estrellas(self.canvas_canal, 100, 120, 12)

        self.flecha = self.canvas_canal.create_line(
            10,
            60,
            90,
            60,
            arrow=tk.LAST,
            width=4,
            fill="#4a4a6a"
        )

        tk.Label(
            self.frame_canal,
            text="CANAL\nM/M/1",
            bg=self.COLOR_FONDO,
            fg=self.COLOR_ACENTO2,
            font=("Arial", 8, "italic")
        ).pack()

        # =========================================================
        # PC-B
        # =========================================================

        self.frame_pcb = tk.Frame(
            self.main_container,
            bg=self.COLOR_FONDO
        )

        self.frame_pcb.grid(
            row=0,
            column=2,
            sticky="nsew"
        )

        self.canvas_b = tk.Canvas(
            self.frame_pcb,
            width=480,
            height=120,
            bg=self.COLOR_PANEL,
            highlightthickness=1,
            highlightbackground=self.COLOR_ACENTO
        )

        self.canvas_b.pack(pady=5)

        tk.Label(
            self.frame_pcb,
            text="🛰 TERMINAL RECEPTOR - DESENCAPSULAMIENTO",
            bg=self.COLOR_FONDO,
            fg=self.COLOR_TITULO,
            font=("Arial", 9, "bold")
        ).pack()

        self.consola_b = tk.Text(
            self.frame_pcb,
            width=60,
            height=22,
            bg="#000010",
            fg=self.COLOR_ACENTO2,
            font=("Consolas", 9),
            insertbackground=self.COLOR_ACENTO2
        )

        self.consola_b.pack(pady=5)

        # =========================================================
        # NOMBRES DE LAS CAPAS
        # =========================================================

        self.nombres = [
            "APL",
            "PRE",
            "SES",
            "TRA",
            "RED",
            "ENL",
            "FIS"
        ]

        self.rects_a = []
        self.rects_b = []

        self._dibujar_nodos()

    # =============================================================
    # DIBUJAR UN CAMPO DE ESTRELLAS ALEATORIO EN UN CANVAS
    # =============================================================

    def _dibujar_estrellas(self, canvas, ancho, alto, cantidad):

        for _ in range(cantidad):

            x = random.randint(0, ancho)
            y = random.randint(0, alto)
            r = random.choice([1, 1, 1, 2])

            brillo = random.choice(
                ["#ffffff", "#cfd8ff", "#8a5cf6", "#ffd166"]
            )

            canvas.create_oval(
                x, y, x + r, y + r,
                fill=brillo,
                outline=""
            )

    # =============================================================
    # DIBUJAR LAS 7 CAPAS
    # =============================================================

    def _dibujar_nodos(self):

        # PC-A: recorrido de capa 7 a capa 1

        for i in range(7):

            x = 15 + (i * 65)

            r = self.canvas_a.create_rectangle(
                x,
                30,
                x + 55,
                90,
                outline=self.COLOR_ACENTO,
                fill=self.COLOR_PANEL
            )

            self.canvas_a.create_text(
                x + 27,
                60,
                text=self.nombres[i],
                font=("Arial", 7, "bold"),
                fill=self.COLOR_TEXTO
            )

            self.rects_a.append(r)

        # PC-B: recorrido de capa 1 a capa 7

        for i in range(7):

            x = 15 + (i * 65)

            r = self.canvas_b.create_rectangle(
                x,
                30,
                x + 55,
                90,
                outline=self.COLOR_ACENTO,
                fill=self.COLOR_PANEL
            )

            self.canvas_b.create_text(
                x + 27,
                60,
                text=self.nombres[6 - i],
                font=("Arial", 7, "bold"),
                fill=self.COLOR_TEXTO
            )

            self.rects_b.append(r)

    # =============================================================
    # ESCRIBIR EN CONSOLA PC-A
    # =============================================================

    def log_a(self, msg):

        self.consola_a.insert(
            tk.END,
            msg + "\n"
        )

        self.consola_a.see(tk.END)

        self.root.update()

    # =============================================================
    # ESCRIBIR EN CONSOLA PC-B
    # =============================================================

    def log_b(self, msg):

        self.consola_b.insert(
            tk.END,
            msg + "\n"
        )

        self.consola_b.see(tk.END)

        self.root.update()

    # =============================================================
    # REINICIAR SIMULADOR
    # =============================================================

    def resetear(self):

        self.consola_a.delete(
            1.0,
            tk.END
        )

        self.consola_b.delete(
            1.0,
            tk.END
        )

        self.canvas_canal.itemconfig(
            self.flecha,
            fill="#4a4a6a"
        )

        for r in self.rects_a:

            self.canvas_a.itemconfig(
                r,
                fill=self.COLOR_PANEL
            )

        for r in self.rects_b:

            self.canvas_b.itemconfig(
                r,
                fill=self.COLOR_PANEL
            )

    # =============================================================
    # ENCAPSULAMIENTO
    # =============================================================

    def encapsular_capa(self, datos, capa):

        if capa == 7:

            return "[APP] " + datos

        elif capa == 6:

            datos_codificados = base64.b64encode(
                datos.encode()
            ).decode()

            return "[PRE] " + datos_codificados

        elif capa == 5:

            return "[SES][ID=001] " + datos

        elif capa == 4:

            return "[TRA][PUERTO=5000] " + datos

        elif capa == 3:

            return "[RED][IP=192.168.1.10] " + datos

        elif capa == 2:

            return "[ENL][MAC=AA:BB:CC:DD:EE:FF] " + datos

        elif capa == 1:

            bits = " ".join(
                format(byte, "08b")
                for byte in datos.encode()
            )

            return "[FIS] " + bits

        return datos

    # =============================================================
    # DESENCAPSULAMIENTO
    # =============================================================

    def desencapsular_capa(self, datos, capa):

        if capa == 1:

            datos = datos.replace(
                "[FIS] ",
                ""
            )

            grupos = datos.split()

            texto = bytes(
                int(grupo, 2)
                for grupo in grupos
            ).decode()

            return texto

        elif capa == 2:

            return datos.replace(
                "[ENL][MAC=AA:BB:CC:DD:EE:FF] ",
                ""
            )

        elif capa == 3:

            return datos.replace(
                "[RED][IP=192.168.1.10] ",
                ""
            )

        elif capa == 4:

            return datos.replace(
                "[TRA][PUERTO=5000] ",
                ""
            )

        elif capa == 5:

            return datos.replace(
                "[SES][ID=001] ",
                ""
            )

        elif capa == 6:

            datos = datos.replace(
                "[PRE] ",
                ""
            )

            return base64.b64decode(
                datos.encode()
            ).decode()

        elif capa == 7:

            return datos.replace(
                "[APP] ",
                ""
            )

        return datos

    # =============================================================
    # TRANSMISIÓN COMPLETA
    # =============================================================

    def transmitir(self):

        msg = self.entrada.get().strip()

        if not msg:

            messagebox.showwarning(
                "Advertencia",
                "Ingrese un mensaje para transmitir."
            )

            return

        self.resetear()

        # =========================================================
        # INICIO PC-A
        # =========================================================

        self.log_a(
            "=============================================="
        )

        self.log_a(
            "PC-A: INICIO DE TRANSMISIÓN"
        )

        self.log_a(
            f"Mensaje original: {msg}"
        )

        self.log_a(
            "=============================================="
        )

        datos = msg

        # =========================================================
        # RECORRIDO DE 7 A 1
        # =========================================================

        for capa in range(7, 0, -1):

            indice = 7 - capa

            self.canvas_a.itemconfig(
                self.rects_a[indice],
                fill=self.COLOR_ACENTO2
            )

            datos = self.encapsular_capa(
                datos,
                capa
            )

            tiempo_espera = random.uniform(
                0.01,
                0.10
            )

            self.log_a(
                f"\nCapa {capa}: {self.nombre_capa(capa)}"
            )

            self.log_a(
                "Información agregada:"
            )

            self.log_a(
                datos[:120]
            )

            self.log_a(
                f"Tiempo simulado: {tiempo_espera:.4f}s"
            )

            time.sleep(0.5)

            self.canvas_a.itemconfig(
                self.rects_a[indice],
                fill=self.COLOR_EXITO
            )

        # =========================================================
        # CANAL DE TRANSMISIÓN
        # =========================================================

        self.log_a(
            "\n>>> ENCAPSULAMIENTO COMPLETADO"
        )

        self.log_a(
            ">>> Enviando datos al canal..."
        )

        self.canvas_canal.itemconfig(
            self.flecha,
            fill=self.COLOR_ACENTO2
        )

        time.sleep(1)

        self.canvas_canal.itemconfig(
            self.flecha,
            fill=self.COLOR_EXITO
        )

        # =========================================================
        # PC-B
        # =========================================================

        self.log_b(
            "=============================================="
        )

        self.log_b(
            "PC-B: DATOS RECIBIDOS"
        )

        self.log_b(
            "=============================================="
        )

        self.log_b(
            "La trama llegó correctamente al receptor."
        )

        # =========================================================
        # DESENCAPSULAMIENTO 1 A 7
        # =========================================================

        for capa in range(1, 8):

            indice = capa - 1

            self.canvas_b.itemconfig(
                self.rects_b[indice],
                fill=self.COLOR_ACENTO2
            )

            tiempo_espera = random.uniform(
                0.01,
                0.10
            )

            self.log_b(
                f"\nCapa {capa}: {self.nombre_capa(capa)}"
            )

            self.log_b(
                "Eliminando información de la capa..."
            )

            datos = self.desencapsular_capa(
                datos,
                capa
            )

            self.log_b(
                "Datos actuales:"
            )

            self.log_b(
                datos[:120]
            )

            self.log_b(
                f"Tiempo simulado: {tiempo_espera:.4f}s"
            )

            time.sleep(0.5)

            self.canvas_b.itemconfig(
                self.rects_b[indice],
                fill=self.COLOR_ACENTO2
            )

        # =========================================================
        # MENSAJE FINAL
        # =========================================================

        self.log_b(
            "\n=============================================="
        )

        self.log_b(
            "TRANSMISIÓN COMPLETADA CORRECTAMENTE"
        )

        self.log_b(
            f"Mensaje recuperado: {datos}"
        )

        self.log_b(
            "=============================================="
        )

    # =============================================================
    # NOMBRE DE CADA CAPA
    # =============================================================

    def nombre_capa(self, capa):

        nombres = {

            7: "APLICACIÓN",

            6: "PRESENTACIÓN",

            5: "SESIÓN",

            4: "TRANSPORTE",

            3: "RED",

            2: "ENLACE DE DATOS",

            1: "FÍSICA"
        }

        return nombres[capa]


# =============================================================
# PROGRAMA PRINCIPAL
# =============================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = SimuladorOSI_Alineado(root)

    root.mainloop()
