import tkinter as tk
from random import randint


class CustomButton:
    w: tk.Button

    def __init__(self, shared) -> None:
        self._bind(shared)

        self._build()
    
    def _bind(self, shared) -> None:
        from shared import Shared
        self.shared: Shared = shared
        self.shared.button = self
    
    def _build(self) -> None:
        self.w = tk.Button(self.shared.root.w)
        self.w.configure(text="button", command=self._action)
        self.w.pack(fill="x")

    def _action(self) -> None:
        text = self.shared.entry.get_value()
        if not text:
            text = randint(0, 99999)

        self.shared.label.set_text(text)

    
