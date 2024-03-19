import customtkinter as ctk
from canvas import *
from PIL import Image, ImageTk
from panels import *
from settings import *


class Menu(ctk.CTkTabview):
    def __init__(self, parent, export_image, channels_var):
        super().__init__(master=parent)
        self.grid(column=0, row=0, sticky='nsew', padx=10, pady=10)

        # create tabs
        self.add("Import")
        self.add("Edit")
        self.add("Export")

        # Widgets
        # PositionFrame(self.tab('Import'))
        EditFrame(self.tab('Edit'), channels_var)
        ExportFrame(self.tab('Export'), export_image)


class EditFrame(ctk.CTkFrame):
    def __init__(self, parent, channels_var):
        super().__init__(master=parent, fg_color='transparent')
        self.pack(expand=True, fill='both')

        DropdownPanel(self, channels_var, CHANNELS)
        AlphaPanel(self)
        EditPanel(self)


class ExportFrame(ctk.CTkFrame):
    def __init__(self, parent, export_image):
        super().__init__(master=parent, fg_color='transparent')
        self.pack(expand=True, fill='both')

        self.name_string = ctk.StringVar()
        self.file_string = ctk.StringVar(value='jpg')
        self.path_string = ctk.StringVar()

        FileNamePanel(self, self.name_string, self.file_string)
        FilePathPanel(self, self.path_string)
        SaveButton(self, export_image, self.name_string,
                   self.file_string, self.path_string)
