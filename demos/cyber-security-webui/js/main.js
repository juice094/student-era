// Progress bar
const progressBar = document.getElementById('progressBar');
window.addEventListener('scroll', () => {
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
    progressBar.style.width = progress + '%';
});

// Nav scroll shadow
const nav = document.getElementById('navbar');
window.addEventListener('scroll', () => {
    if (window.scrollY > 10) nav.classList.add('scrolled');
    else nav.classList.remove('scrolled');
});

// Active nav link highlighting
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav-links a[href^="#"]');
window.addEventListener('scroll', () => {
    let current = '';
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        if (window.scrollY >= sectionTop - 120) {
            current = section.getAttribute('id');
        }
    });
    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === '#' + current) {
            link.classList.add('active');
        }
    });
});

// Fade in animation
const fadeObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            fadeObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.08, rootMargin: '0px 0px -20px 0px' });
document.querySelectorAll('.fade-in').forEach(el => fadeObserver.observe(el));

// Quiz interaction
const quizContainer = document.querySelector('.quiz-container');
if (quizContainer) {
    quizContainer.addEventListener('click', (e) => {
        const item = e.target.closest('.quiz-item');
        if (item) {
            const isActive = item.classList.contains('active');
            document.querySelectorAll('.quiz-item').forEach(q => {
                q.classList.remove('active');
                q.setAttribute('aria-expanded', 'false');
            });
            if (!isActive) {
                item.classList.add('active');
                item.setAttribute('aria-expanded', 'true');
            }
        }
    });
    quizContainer.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
            const item = e.target.closest('.quiz-item');
            if (item) { e.preventDefault(); item.click(); }
        }
    });
}

// File challenge
let identifiedCount = 0;
function checkFile(card) {
    if (card.classList.contains('revealed')) return;
    const isSafe = card.dataset.safe === 'true';
    card.classList.add('revealed', isSafe ? 'correct' : 'wrong');
    card.querySelector('.file-verdict').classList.remove('hidden');
    identifiedCount++;
    document.getElementById('challenge-score').textContent = '已识别 ' + identifiedCount + ' / 6';
}

// Symptom checklist
function toggleSymptom(label) {
    const cb = label.querySelector('input[type=checkbox]');
    cb.checked = !cb.checked;
    if (cb.checked) label.classList.add('checked');
    else label.classList.remove('checked');
    const checked = document.querySelectorAll('.symptom-item input:checked').length;
    const result = document.getElementById('symptom-result');
    if (checked === 0) result.textContent = '勾选越多，中毒概率越高。出现第3条则99%确认感染。';
    else if (checked >= 3) result.textContent = '⚠️ 高危：已勾选 ' + checked + ' 项，强烈建议立即进行全盘扫描！';
    else result.textContent = '已勾选 ' + checked + ' 项，请继续保持警惕。';
}
