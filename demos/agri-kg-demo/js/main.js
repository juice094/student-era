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

// ECharts lazy load
const chartConfigs = [
    {
        id: 'chart-model',
        option: {
            tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' } },
            legend: { data: ['Accuracy', 'F1-Score'], bottom: 0, textStyle: { fontSize: 11 } },
            grid: { left: '2%', right: '4%', bottom: '14%', top: '8%', containLabel: true },
            xAxis: { type: 'category', data: ['ERNIE 3.0\n(篇章级)', 'GLM-4-9B\n(篇章级)', 'Qwen2.5-32B\n(无PPE)', 'Qwen2.5-32B\n(+PPE)', 'Qwen2.5-72B\n(基线)'], axisLabel: { fontSize: 10, interval: 0 } },
            yAxis: { type: 'value', max: 100, axisLabel: { formatter: '{value}%', fontSize: 10 } },
            series: [
                { name: 'Accuracy', type: 'bar', data: [87.04, 87.04, null, null, null], itemStyle: { color: '#059669', borderRadius: [4, 4, 0, 0] }, label: { show: true, position: 'top', formatter: '{c}%', fontSize: 10 } },
                { name: 'F1-Score', type: 'bar', data: [null, null, 77.9, 85.1, 76.6], itemStyle: { color: '#0369a1', borderRadius: [4, 4, 0, 0] }, label: { show: true, position: 'top', formatter: '{c}%', fontSize: 10 } }
            ]
        }
    },
    {
        id: 'chart-retrieval',
        option: {
            tooltip: { trigger: 'axis' },
            legend: { data: ['人工查询', 'LLM模拟查询'], bottom: 0, textStyle: { fontSize: 11 } },
            grid: { left: '2%', right: '4%', bottom: '14%', top: '8%', containLabel: true },
            xAxis: { type: 'category', data: ['NaiveRAG', 'GraphRAG', 'LightRAG', 'AgenticGraphRAG'], axisLabel: { fontSize: 10 } },
            yAxis: { type: 'value', max: 100, axisLabel: { formatter: '{value}%', fontSize: 10 } },
            series: [
                { name: '人工查询', type: 'bar', data: [null, null, null, 86], itemStyle: { color: '#059669', borderRadius: [4, 4, 0, 0] }, label: { show: true, formatter: '{c}%', position: 'top', fontSize: 10 }, markArea: { data: [[{ name: '数据待补充', xAxis: 'NaiveRAG', itemStyle: { color: 'rgba(148, 163, 184, 0.15)' } }, { xAxis: 'LightRAG' }]] } },
                { name: 'LLM模拟查询', type: 'bar', data: [null, null, null, 89.33], itemStyle: { color: '#0369a1', borderRadius: [4, 4, 0, 0] }, label: { show: true, formatter: '{c}%', position: 'top', fontSize: 10 } }
            ]
        }
    }
];

const chartInstances = {};
const chartObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting && !chartInstances[entry.target.id]) {
            const config = chartConfigs.find(c => c.id === entry.target.id);
            if (config) {
                const chart = echarts.init(entry.target);
                chart.setOption(config.option);
                chartInstances[entry.target.id] = chart;
            }
            chartObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.1 });
chartConfigs.forEach(c => {
    const el = document.getElementById(c.id);
    if (el) chartObserver.observe(el);
});

window.addEventListener('resize', () => {
    Object.values(chartInstances).forEach(chart => chart.resize());
});

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
            if (item) {
                e.preventDefault();
                item.click();
            }
        }
    });
}