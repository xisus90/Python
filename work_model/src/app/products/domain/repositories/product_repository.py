from abc import ABC, abstractmethod
from typing import List, Optional

from app.products.domain.entities.product import Product

class ProductRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[Product]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[Product]:
        pass

    @abstractmethod
    def create(self, product: Product) -> Product:
        pass

    @abstractmethod
    def update(self, product_id: int, product: Product) -> Optional[Product]:
        pass

    @abstractmethod
    def delete(self, product_id: int) -> bool:
        pass