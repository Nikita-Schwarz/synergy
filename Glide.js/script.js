const glide = new Glide('.glide', {
    type: 'carousel',
    perPage: 1,
    autoplay: 3000,
    hoverpause: true,
}).mount();

const updateCounter = () => {
    const currentSlide = glide.index + 1; // +1 для отображения числа начиная с 1
    const totalSlides = glide.length;
    document.getElementById('counter').textContent = `Изображение ${currentSlide} из ${totalSlides}`;
};

// Обновление счетчика при изменении слайда
glide.on(['mount.after', 'run.after'], updateCounter);

// Инициализация счетчика
updateCounter();