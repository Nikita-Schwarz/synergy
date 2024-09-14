const images = [
    'image1.jpeg',
    'image2.jpeg',
    'image3.jpeg',
    'image4.jpeg',
    'image5.jpeg'
];

let currentIndex = 0;

const slide = document.getElementById('slide');
const counter = document.getElementById('counter');
const prevButton = document.getElementById('prev');
const nextButton = document.getElementById('next');

function updateSlider() {
    slide.src = images[currentIndex];
    counter.textContent = `Изображение ${currentIndex + 1} из ${images.length}`;
}

nextButton.addEventListener('click', () => {
    currentIndex = (currentIndex + 1) % images.length;
    updateSlider();
});

prevButton.addEventListener('click', () => {
    currentIndex = (currentIndex - 1 + images.length) % images.length;
    updateSlider();
});

// Инициализация слайдера
updateSlider();