// Навигация между разделами
document.querySelectorAll('nav a').forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault();
        
        // Скрыть все разделы
        document.querySelectorAll('.section').forEach(section => {
            section.style.display = 'none';
        });
        
        // Показать выбранный раздел
        const targetId = this.getAttribute('href');
        document.querySelector(targetId).style.display = 'block';
        
        // Прокрутить к разделу
        window.scrollTo({
            top: document.querySelector(targetId).offsetTop - 20,
            behavior: 'smooth'
        });
        
        // Обновить активную ссылку
        document.querySelectorAll('nav a').forEach(navLink => {
            navLink.classList.remove('active');
        });
        this.classList.add('active');
    });
});

// Показать главную страницу при загрузке
document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#home').style.display = 'block';
});
