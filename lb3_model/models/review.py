class Review:
    def __init__(self, id: int, user, product, rating: int, comment: str = ""):
        self.id = id
        self.user = user
        self.product = product
        self.rating = rating
        self.comment = comment

    def __str__(self):
        return f"Review(user={self.user.full_name}, product={self.product.name}, rating={self.rating}/5)"
