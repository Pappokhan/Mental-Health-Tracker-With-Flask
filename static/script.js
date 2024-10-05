// script.js

document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector('form');

    // Simple validation to ensure all questions are answered
    form.addEventListener('submit', function (event) {
        const selects = form.querySelectorAll('select');
        let allAnswered = true;

        selects.forEach(select => {
            if (select.value === "") {
                allAnswered = false;
                select.classList.add('error');  // Add an error class for visual feedback
            } else {
                select.classList.remove('error');  // Remove error class if answered
            }
        });

        if (!allAnswered) {
            event.preventDefault(); // Prevent form submission if not all answered
            alert("Please answer all questions before submitting.");
        }
    });
});