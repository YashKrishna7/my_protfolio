// Scroll reveal
const reveals = document.querySelectorAll('.section');
const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => {
        if (e.isIntersecting) {
            e.target.querySelectorAll('.project-card, .skill-group, .edu-card, .exp-card').forEach((el, i) => {
                el.classList.add('reveal');
                setTimeout(() => el.classList.add('visible'), i * 80);
            });
        }
    });
}, { threshold: 0.1 });

document.querySelectorAll('.section').forEach(s => observer.observe(s));

// Mobile nav
const burger = document.getElementById('burger');
const navLinks = document.querySelector('.nav-links');
burger.addEventListener('click', () => navLinks.classList.toggle('open'));

// Active nav highlight on scroll
const sections = document.querySelectorAll('section[id]');
window.addEventListener('scroll', () => {
    const scrollY = window.scrollY;
    sections.forEach(sec => {
        const top = sec.offsetTop - 100;
        const id = sec.getAttribute('id');
        const link = document.querySelector(`.nav-links a[href="#${id}"]`);
        if (link) {
            if (scrollY >= top && scrollY < top + sec.offsetHeight) {
                link.style.color = 'var(--accent)';
            } else {
                link.style.color = '';
            }
        }
    });
});
