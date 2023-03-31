from uuid import uuid4

import tkinter as tk


class ComplexWidget:
    w: tk.Frame
    button: tk.Button
    label: tk.Label
    
    def __init__(self, shared) -> None:
        self._bind(shared)
        self._build()

    def _bind(self, shared) -> None:
        from shared import Shared
        self.shared: Shared = shared
        self.shared.complex = self

    def _build(self) -> None:
        self.w = tk.Frame(self.shared.root.w)
        self.w.pack(fill="x")

        self.label = tk.Label(self.w)
        self.label.pack()

        self.button = tk.Button(self.w, text="Generate UUID4", command=self._action)
        self.button.pack()
    
    def _action(self) -> None:
        self.label.configure(text=str(uuid4()))
    
