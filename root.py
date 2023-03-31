import tkinter as tk

from label import CustomLabel
from button import CustomButton
from entry import CustomEntry
from complex_widget import ComplexWidget


class MainWindow:
    w: tk.Tk
    
    def __init__(self) -> None:
        self._bind()
        self._build()
        self._create_widgets()
        self.w.mainloop()

    def _bind(self) -> None:
        from shared import Shared
        self.shared = Shared()
        self.shared.root = self

    def _build(self) -> None:
        self.w = tk.Tk()
        self.w.title("New window")
        self.w.geometry("600x400")
    
    def _create_widgets(self) -> None:
        CustomLabel(self.shared)
        CustomEntry(self.shared)
        CustomButton(self.shared)
        ComplexWidget(self.shared)





    
