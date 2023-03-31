import tkinter as tk


class CustomLabel:
    w: tk.Label
    
    def __init__(self, shared) -> None:
        self._bind(shared)
        self._build()

    def _bind(self, shared) -> None:
        from shared import Shared
        self.shared: Shared = shared
        self.shared.label = self

    def _build(self) -> None:
        self.w = tk.Label(self.shared.root.w)
        self.w.pack(fill="x")
    
    def set_text(self, text: str) -> None:
        self.w.configure(text=text)
    
