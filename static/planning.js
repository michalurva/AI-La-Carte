document.addEventListener('DOMContentLoaded', function () {
    var socket = io.connect(location.origin);

    socket.on('connect', function () {
        socket.emit('start_planning');
    });

    socket.on('planning_done', function (data) {
        console.log(data);
        // Update the UI with the received data
        socket.disconnect(); // Disconnect the socket once data is received
    });
});

// Get the loader and recipe button elements by their IDs
const loader = document.getElementById("loader");
const recipeBtn = document.getElementById("recipe-btn");

// Initially hide the recipe button
recipeBtn.style.display = "none";

// Listen for the 'planning_done' event emitted by the server
const socket = io.connect(location.origin);
socket.on("planning_done", () => {
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
});
