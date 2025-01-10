// Add smooth scrolling for the History link (example)
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});


function updateSliderValue(value) {
    document.getElementById('sliderValue').textContent = value;
}