document.addEventListener('DOMContentLoaded', function () {
    // Get the loader and recipe button elements by their IDs
    const loader = document.getElementById("loader");
    const recipeBtn = document.getElementById("recipe-btn");

    // Initially hide the recipe button
    recipeBtn.style.display = "none";

    startPlanning();
});

function startPlanning() {
    fetch('/start_planning', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
        planningDone();
    })
    .catch((error) => {
        console.error('Error during planning:', error);
    });
}

function planningDone() {
    // Get the loader and recipe button elements by their IDs
    const loader = document.getElementById("loader");
    const recipeBtn = document.getElementById("recipe-btn");

    // Fade out the loader
    loader.style.transition = "opacity 1s";
    loader.style.opacity = 0;

    // Remove the loader element after the fade-out animation is complete
    setTimeout(() => {
        loader.remove();
    }, 1000);

    // Fade in the recipe button
    recipeBtn.style.transition = "opacity 1s";
    recipeBtn.style.display = "inline-block";
    setTimeout(() => {
        recipeBtn.style.opacity = 1;
    }, 100);
}
