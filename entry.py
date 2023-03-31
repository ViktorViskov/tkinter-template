import tkinter as tk


class CustomEntry:
    w: tk.Entry

    def __init__(self, shared) -> None:
        self._bind(shared)
        self._build()

    def _bind(self, shared) -> None:
        from shared import Shared
        self.shared: Shared = shared
        self.shared.entry = self

    def _build(self) -> None:
        self.w = tk.Entry(self.shared.root.w)
        self.w.pack(fill="x")
    
    def get_value(self) -> str:
        text = self.w.get()
        self.w.delete(0, tk.END)
        return text

    
