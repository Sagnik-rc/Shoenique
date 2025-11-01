// Example: Add to cart click functionality
document.addEventListener("DOMContentLoaded", () => {
  const cartButtons = document.querySelectorAll(".add-cart");

  cartButtons.forEach(btn => {
    btn.addEventListener("click", () => {
      const productId = btn.dataset.id;
      alert(`Product ${productId} added to cart!`);
      // Later: send POST request to Django backend to add to cart
    });
  });
});
