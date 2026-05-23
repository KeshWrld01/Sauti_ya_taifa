// ── NAVBAR SCROLL EFFECT ──
window.addEventListener('scroll', () => {
  const navbar = document.querySelector('.navbar');
  if (window.scrollY > 50) {
    navbar.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled');
  }
});

// ── MOBILE MENU ──
function toggleMenu() {
  const links = document.querySelector('.nav-links');
  links.classList.toggle('open');
}

// ── SCROLL ANIMATIONS ──
const observerOptions = {
  threshold: 0.15,
  rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('animate-in');
      observer.unobserve(entry.target);
    }
  });
}, observerOptions);

document.addEventListener('DOMContentLoaded', () => {

  // Observe all animatable elements
  const animatables = document.querySelectorAll(
    '.card, .mission-card, .school-card, .course-card, .memorial-card, .solidarity-card, .resource-card, .right-card, .lesson-block, .stat-item, .section-title, .section-subtitle, .hero-title, .hero-subtitle, .hero-buttons, .donate-cta-text, .families-text, .submit-wrapper, .message-form-wrapper'
  );

  animatables.forEach((el, i) => {
    el.style.transitionDelay = `${(i % 4) * 0.1}s`;
    observer.observe(el);
  });

  // ── HERO TEXT ANIMATION ──
  const heroTitle = document.querySelector('.hero-title');
  if (heroTitle) {
    heroTitle.classList.add('hero-animate');
  }

  // ── COUNTER ANIMATION ──
  const counters = document.querySelectorAll('.stat-number');
  const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        animateCounter(entry.target);
        counterObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });

  counters.forEach(counter => counterObserver.observe(counter));

  // ── BUTTON RIPPLE ──
  document.querySelectorAll('.btn').forEach(btn => {
    btn.addEventListener('click', function(e) {
      const ripple = document.createElement('span');
      ripple.classList.add('ripple');
      const rect = this.getBoundingClientRect();
      ripple.style.left = `${e.clientX - rect.left}px`;
      ripple.style.top = `${e.clientY - rect.top}px`;
      this.appendChild(ripple);
      setTimeout(() => ripple.remove(), 700);
    });
  });

  // ── CANDLE FLICKER ──
  document.querySelectorAll('.memorial-candle').forEach(candle => {
    setInterval(() => {
      candle.style.opacity = (Math.random() * 0.5 + 0.5).toFixed(2);
    }, 300);
  });

  // ── NAVBAR ACTIVE LINK ──
  const currentPath = window.location.pathname;
  document.querySelectorAll('.nav-links a').forEach(link => {
    if (link.getAttribute('href') === currentPath) {
      link.classList.add('active-link');
    }
  });

  // ── TYPING EFFECT ON HERO ──
  const typingEl = document.querySelector('.hero-title');
  if (typingEl) {
    typingEl.style.opacity = '1';
  }

});

// ── COUNTER FUNCTION ──
function animateCounter(el) {
  const text = el.textContent;
  const hasPlus = text.includes('+');
  const hasK = text.includes('K');
  const hasPercent = text.includes('%');

  // Extract number
  let target = parseFloat(text.replace(/[^0-9.]/g, ''));
  if (isNaN(target)) return;

  let start = 0;
  const duration = 2000;
  const step = 16;
  const increment = target / (duration / step);

  const timer = setInterval(() => {
    start += increment;
    if (start >= target) {
      start = target;
      clearInterval(timer);
    }

    let display = Math.floor(start);
    if (hasK) display = (start / 1).toFixed(0);

    el.textContent =
      (hasK ? display + 'K' : display) +
      (hasPlus ? '+' : '') +
      (hasPercent ? '%' : '');
  }, step);
}

// ── SMOOTH SCROLL FOR ANCHOR LINKS ──
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});

// ── PAGE TRANSITION ──
document.addEventListener('DOMContentLoaded', () => {
  document.body.classList.add('page-loaded');
});