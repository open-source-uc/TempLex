from fastapi import HTTPException, status


class NotFoundException(HTTPException):
    def __init__(self, alias: str) -> None:
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"El dat {alias} no existe"
        )
