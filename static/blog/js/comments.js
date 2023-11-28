
document.addEventListener("DOMContentLoaded", function () {
    // Initially hide the comments container
    var commentsContainer = document.getElementById("comments-container");
    commentsContainer.style.display = "none";

    // Add an event listener to the "Show Comments" link
    var toggleCommentsLink = document.getElementById("toggle-comments");
    toggleCommentsLink.addEventListener("click", function (event) {
        event.preventDefault();
        if (commentsContainer.style.display === "none") {
        commentsContainer.style.display = "block";
        } else {
        commentsContainer.style.display = "none";
        }
    });
    });