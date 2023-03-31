class mathError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return "Erreur arguments mathématique (determinant nul / Erreur de dimension)"