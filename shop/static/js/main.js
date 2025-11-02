/* SHOENIQUE MAIN.JS*/

// Navbar background change on scroll
window.addEventListener("scroll", () => {
  const nav = document.querySelector(".custom-navbar");
  if (window.scrollY > 50) {
    nav.classList.add("scrolled");
  } else {
    nav.classList.remove("scrolled");
  }
});


document.addEventListener('DOMContentLoaded', function() {
    const navbar = document.querySelector('.custom-navbar');
    
    window.addEventListener('scroll', function() {
        if (window.scrollY > 100) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });
});

/* SMOOTH SCROLL EFFECT */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute("href"));
    if (target) {
      window.scrollTo({
        top: target.offsetTop - 70, // offset for navbar height
        behavior: "smooth",
      });
    }
  });
});

/* =========================BONUS: CART BUTTON ANIMATION*/
const cartBtn = document.querySelector(".cart-btn");

if (cartBtn) {
  cartBtn.addEventListener("click", () => {
    // Add temporary class for animation
    cartBtn.classList.add("clicked");

    // Create sparkle effect
    const sparkle = document.createElement("span");
    sparkle.classList.add("sparkle");
    cartBtn.appendChild(sparkle);

    // Remove sparkle and class after animation
    setTimeout(() => {
      cartBtn.classList.remove("clicked");
      sparkle.remove();
    }, 700);
  });
}

/* HERO TEXT FADE-IN EFFECT */
window.addEventListener("load", () => {
  const heroContent = document.querySelector(".hero-content");
  if (heroContent) {
    heroContent.style.opacity = 0;
    heroContent.style.transform = "translateY(20px)";
    setTimeout(() => {
      heroContent.style.transition = "all 1s ease";
      heroContent.style.opacity = 1;
      heroContent.style.transform = "translateY(0)";
    }, 300);
  }
});

document.addEventListener('DOMContentLoaded', function() {
    // Intersection Observer for scroll animations
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, {
        threshold: 0.1
    });

    // Observe all elements with fade-in class
    document.querySelectorAll('.fade-in').forEach((element) => {
        observer.observe(element);
    });
});
