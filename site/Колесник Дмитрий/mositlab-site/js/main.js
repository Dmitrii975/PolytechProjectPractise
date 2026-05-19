function showPage(id) {
    document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
    document.querySelectorAll('.nav-links a').forEach(a => a.classList.remove('active'));
    const page = document.getElementById('page-' + id);
    if (page) {
        page.classList.add('active');
        const fi = page.querySelector('.fade-in');
        if (fi) {
            fi.style.animation = 'none';
            fi.offsetHeight;
            fi.style.animation = '';
        }
    }
    const navLink = document.getElementById('nav-' + id);
    if (navLink) navLink.classList.add('active');
    window.scrollTo({ top: 0, behavior: 'smooth' });
    return false;
}
function animateCounters() {
    document.querySelectorAll('.stat-num').forEach(el => {
        const text = el.textContent;
        const match = text.match(/[\d.]+/);
        if (!match) return;
        const target = parseFloat(match[0]);
        const suffix = text.replace(match[0], '');
        let start = 0;
        const duration = 1500;
        const step = 16;
        const increment = target / (duration / step);
        const timer = setInterval(() => {
            start += increment;
            if (start >= target) {
                start = target;
                clearInterval(timer);
            }
            el.textContent = (Number.isInteger(target) ? Math.round(start) : start.toFixed(1)) + suffix;
        }, step);
    });
}
document.addEventListener('DOMContentLoaded', () => {
    animateCounters();
    document.querySelectorAll('.card, .team-card, .res-card, .post').forEach(card => {
        card.addEventListener('mousemove', e => {
            const rect = card.getBoundingClientRect();
            const x = ((e.clientX - rect.left) / rect.width) * 100;
            const y = ((e.clientY - rect.top) / rect.height) * 100;
            card.style.background = `radial-gradient(circle at ${x}% ${y}%, rgba(34,197,94,0.08), var(--card) 70%)`;
        });
        card.addEventListener('mouseleave', () => {
            card.style.background = '';
        });
    });
});