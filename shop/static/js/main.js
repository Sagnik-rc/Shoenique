/* ================= SHOENIQUE MAIN.JS ================= */

/* --------------------------------------------------
   ✅ NAVBAR SCROLL EFFECT
-------------------------------------------------- */
window.addEventListener("scroll", () => {
    const nav = document.querySelector(".custom-navbar");
    if (!nav) return;

    nav.classList.toggle("scrolled", window.scrollY > 80);
});

/* --------------------------------------------------
   ✅ SMOOTH SCROLLING FOR # LINKS
-------------------------------------------------- */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute("href"));
        if (!target) return;

        window.scrollTo({
            top: target.offsetTop - 70,
            behavior: "smooth",
        });
    });
});

/* --------------------------------------------------
   ✅ HERO SECTION ANIMATION
-------------------------------------------------- */
window.addEventListener("load", () => {
    const heroContent = document.querySelector(".hero-content");
    if (heroContent) {
        heroContent.style.opacity = 0;
        heroContent.style.transform = "translateY(20px)";
        setTimeout(() => {
            heroContent.style.transition = "all 1s ease";
            heroContent.style.opacity = 1;
            heroContent.style.transform = "translateY(0)";
        }, 200);
    }
});

/* --------------------------------------------------
   ✅ SCROLL FADE-IN ELEMENTS
-------------------------------------------------- */
document.addEventListener("DOMContentLoaded", function () {
    const observer = new IntersectionObserver(
        entries => {
            entries.forEach(entry => {
                if (entry.isIntersecting) entry.target.classList.add("visible");
            });
        },
        { threshold: 0.2 }
    );

    document.querySelectorAll(".fade-in").forEach(el => observer.observe(el));
});

/* ==================================================
        ✅ CART MODULE (BEST PRACTICE)
================================================== */
const Cart = {
    get() {
        return JSON.parse(localStorage.getItem("cart")) || [];
    },

    save(cart) {
        localStorage.setItem("cart", JSON.stringify(cart));
        Cart.updateCounter();
    },

    add(item) {
        let cart = Cart.get();
        let existing = cart.find(p => p.id == item.id);

        if (existing) {
            existing.quantity += 1;
        } else {
            cart.push(item);
        }

        Cart.save(cart);

        Swal.fire({
            title: "Added to Cart!",
            text: `${item.name} has been added.`,
            icon: "success",
            timer: 1500,
            showConfirmButton: false,
        });
    },

    remove(index) {
        let cart = Cart.get();
        cart.splice(index, 1);
        Cart.save(cart);
        Cart.render();
    },

    changeQty(index, amount) {
        let cart = Cart.get();
        if (cart[index].quantity + amount <= 0) return;

        cart[index].quantity += amount;
        Cart.save(cart);
        Cart.render();
    },

    getTotal() {
        return Cart.get().reduce((sum, p) => sum + p.price * p.quantity, 0);
    },

    updateCounter() {
        const count = Cart.get().reduce((sum, p) => sum + p.quantity, 0);
        const badge = document.getElementById("cart-count");

        if (badge) badge.innerText = count;
    },

    render() {
        let cartTable = document.getElementById("cart-items");
        let emptyBox = document.getElementById("empty-cart");
        let grandTotal = document.getElementById("grand-total");

        if (!cartTable) return; // Not on cart page

        let cart = Cart.get();
        cartTable.innerHTML = "";

        if (cart.length === 0) {
            emptyBox.style.display = "block";
            grandTotal.innerText = "0";
            return;
        }

        emptyBox.style.display = "none";

        cart.forEach((item, idx) => {
            cartTable.innerHTML += `
                <tr>
                    <td><img src="${item.image}" width="70" class="rounded"></td>
                    <td>${item.name}</td>
                    <td>₹${item.price}</td>
                    <td>
                        <button class="btn btn-light btn-sm" onclick="Cart.changeQty(${idx}, -1)">-</button>
                        <span class="mx-2">${item.quantity}</span>
                        <button class="btn btn-light btn-sm" onclick="Cart.changeQty(${idx}, 1)">+</button>
                    </td>
                    <td>₹${item.price * item.quantity}</td>
                    <td>
                        <button onclick="Cart.remove(${idx})" class="btn btn-danger btn-sm">
                            <i class="fa fa-trash"></i>
                        </button>
                    </td>
                </tr>
            `;
        });

        grandTotal.innerText = Cart.getTotal();
    }
};

/* --------------------------------------------------
   ✅ Initialize Cart Counter Everywhere
-------------------------------------------------- */
document.addEventListener("DOMContentLoaded", Cart.updateCounter);

/* --------------------------------------------------
   ✅ Render Cart Page (if cart.html)
-------------------------------------------------- */
document.addEventListener("DOMContentLoaded", Cart.render);

/* ==================================================
        ✅ ADD TO CART HANDLER
================================================== */
document.addEventListener("click", function (e) {
    if (e.target.classList.contains("add-cart")) {
        let btn = e.target;

        Cart.add({
            id: btn.dataset.id,
            name: btn.dataset.name,
            price: parseFloat(btn.dataset.price),
            image: btn.dataset.image,
            quantity: 1
        });
    }
});

/* ==================================================
        ✅ BUY NOW HANDLER
================================================== */
document.addEventListener("click", function (e) {
    if (e.target.classList.contains("btn-buy-now")) {

        let btn = e.target;

        const item = {
            id: btn.dataset.id,
            name: btn.dataset.name,
            price: parseFloat(btn.dataset.price),
            image: btn.dataset.image,
            quantity: 1
        };

        localStorage.setItem("buy_now_item", JSON.stringify(item));

        window.location.href = "/checkout/";
    }
});
