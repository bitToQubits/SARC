import customtkinter
import tkinter
from PIL import Image
from tkinter import filedialog as fd
from backend import match_face

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title = "SARC"
        self.geometry("1200x600")

        self.main = customtkinter.CTkFrame(self, fg_color="transparent")

        button = customtkinter.CTkButton(master=self, text="Identificar", command=self.seleccionarFoto)
        button.pack(side="bottom", anchor="se", padx=(0,10), pady=(0, 10))

        self.main.pack(side="top", fill="both", expand=True)

        # General info frame
        # Configure grid to center main_frame horizontally
        self.main.grid_columnconfigure(0, weight=1)  # Left spacer
        self.main.grid_columnconfigure(1, weight=0)  # main_frame column
        self.main.grid_columnconfigure(2, weight=1)  # Right spacer

        self.main.grid_rowconfigure(0, weight=0)     # Top spacer
        self.main.grid_rowconfigure(1, weight=0)     # main_frame row
        self.main.grid_rowconfigure(2, weight=0)     # Bottom spacer

        self.main.general_frame = customtkinter.CTkFrame(self.main, fg_color="transparent")
        self.main.general_frame.grid(row=1, column=1, padx=(0, 0), pady=(80, 0))

        # imagen

        titulo = customtkinter.CTkLabel(master=self.main.general_frame, text="SARC")
        titulo.grid(row=0, column=1, padx=(20, 20), pady=(0, 0), sticky="nw")

        photo = customtkinter.CTkImage(light_image=Image.open("elison.png"),
                                  dark_image=Image.open("elison.png"),
                                  size=(350, 355))

        self.main.imagen = customtkinter.CTkLabel(master=self.main.general_frame, image=photo, text="")
        self.main.imagen.grid(row=0, column=1, padx=(20, 20), pady=(30, 0), sticky="ew")

        subtitulo = customtkinter.CTkLabel(master=self.main.general_frame, text="Departamento Nacional de Investigaciones")
        subtitulo.grid(row=0, column=2, padx=(20, 20), pady=(30, 0), sticky="ne")

        self.main.generalInfo_frame = customtkinter.CTkFrame(self.main.general_frame)
        self.main.generalInfo_frame.grid(row=0, column=2, padx=(20, 20), pady=(30, 0), sticky="nw")

        # self.main.nombre_completo_label = customtkinter.CTkLabel(master=self.main.generalInfo_frame, text="Nombre completo:", font=("Arial", 16, "bold"))
        # self.main.nombre_completo_label.grid(row=0, column=2, columnspan=1, padx=10, pady=(10,0), sticky="w")

        self.main.nombre_completo = customtkinter.CTkLabel(master=self.main.generalInfo_frame, text="Elison Perez",font=("Arial", 25))
        self.main.nombre_completo.grid(row=1, column=2, columnspan=1, padx=10, pady=15, sticky="w")

        self.main.sexo_label = customtkinter.CTkLabel(master=self.main.generalInfo_frame, text="Sexo:", font=("Arial", 16, "bold"))
        self.main.sexo_label.grid(row=3, column=2, columnspan=1,padx=(10, 0), pady=(10,0), sticky="w")

        self.main.edad_label = customtkinter.CTkLabel(master=self.main.generalInfo_frame, text="Edad:", font=("Arial", 16, "bold"), anchor="w")
        self.main.edad_label.grid(row=3, column=3, columnspan=1,padx=(0, 10), pady=(10,0), sticky="nw")

        self.main.sexo = customtkinter.CTkLabel(master=self.main.generalInfo_frame, text="M")
        self.main.sexo.grid(row=4, column=2, columnspan=1,padx=(10, 0), pady=2, sticky="w")

        self.main.edad = customtkinter.CTkLabel(master=self.main.generalInfo_frame, text="46")
        self.main.edad.grid(row=4, column=3, columnspan=1,padx=(0, 10), pady=2, sticky="w")

        self.main.ocupacion_label = customtkinter.CTkLabel(master=self.main.generalInfo_frame, text="Ocupación:", font=("Arial", 16, "bold"))
        self.main.ocupacion_label.grid(row=5, column=2, columnspan=1, padx=10, pady=(10,0), sticky="w")

        self.main.ocupacion = customtkinter.CTkLabel(master=self.main.generalInfo_frame, text="Maestro")
        self.main.ocupacion.grid(row=6, column=2, columnspan=1, padx=10, pady=2, sticky="w")

        self.main.telefono_label = customtkinter.CTkLabel(master=self.main.generalInfo_frame, text="Número telefónico:", font=("Arial", 16, "bold"))
        self.main.telefono_label.grid(row=7, column=2, columnspan=1, padx=10, pady=(10,0), sticky="w")

        self.main.telefono = customtkinter.CTkLabel(master=self.main.generalInfo_frame, text="829 777 8919")
        self.main.telefono.grid(row=8, column=2, columnspan=1, padx=10, pady=2, sticky="w")

        self.main.ubicacion_label = customtkinter.CTkLabel(master=self.main.generalInfo_frame, text="Última ubicación conocida", font=("Arial", 16, "bold"))
        self.main.ubicacion_label.grid(row=9, column=2, columnspan=1, padx=10, pady=(10,0), sticky="w")

        self.main.ubicacion = customtkinter.CTkLabel(master=self.main.generalInfo_frame, text="Malecom Fuerte San Gil")
        self.main.ubicacion.grid(row=10, column=2, columnspan=1, padx=10, pady=(2,13), sticky="w")

        #Details info frame

        # self.main.detailsInfo_frame = customtkinter.CTkFrame(self.main.general_frame)
        # self.main.detailsInfo_frame.grid(row=0, column=3, padx=(20, 20), pady=(30, 0), sticky="ne")

        # self.main.nota = customtkinter.CTkLabel(master=self.main.detailsInfo_frame, text="No hay nota para este ciudadano..")
        # self.main.nota.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="w")


    def seleccionarFoto(self):
        filetypes = (
            ('Imágenes JPG', '*.jpg'),
            ('Imágenes PNG', '*.png'),
        )

        filename = fd.askopenfilename(
            title='Abre una imágen',
            initialdir='/',
            filetypes=filetypes
        )
        
        datos_del_ciudadano = match_face(filename)

        if datos_del_ciudadano is not None:
            photo = customtkinter.CTkImage(light_image=Image.open(filename),
                                    dark_image=Image.open(filename),
                                    size=(350, 355))
            self.main.imagen.configure(image=photo)
            self.main.nombre_completo.configure(text=datos_del_ciudadano[1])
            self.main.sexo.configure(text=datos_del_ciudadano[3])
            self.main.edad.configure(text=datos_del_ciudadano[4])
            self.main.credito_social.configure(text=datos_del_ciudadano[5])
            self.main.nota.configure(text=datos_del_ciudadano[6])
            self.main.ubicacion.configure(text=datos_del_ciudadano[8])
            self.main.ocupacion.configure(text=datos_del_ciudadano[7])
        


if __name__ == "__main__":
    
    app = App()
    app.mainloop()