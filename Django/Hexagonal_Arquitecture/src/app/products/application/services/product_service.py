from app.products.domain.repositories.product_repository import ProductRepository
from app.products.domain.entities.product import Product

class ProductService:

     def __init__ (self, product_repository : ProductRepository):
          self.product_repository = product_repository

          def get_all(self) -> list [Product]:
               return self.product_repository.get_all
          
          def get_by_id(self, product_id: int) -> Product:
               return self.product_repository.get_by_id(product_id)
          
          def create(self, product: Product) -> Product:
               return self.product_repository.create(product)
          
          def create(self, product_id: int, product : Product) -> Product:
               return self.product_repository.update(product_id, product)
          
          def delete(self, product_id: int) -> bool:
               return self.product_repository.delete(product_id)
          

               
