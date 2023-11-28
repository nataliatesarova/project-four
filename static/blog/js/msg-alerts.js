// Toggle the messages div
function toggleMessages() {
    $("#django-messages").toggle();
    }

// Show messages div only when there are messages
$(document).ready(function () {
    if ($("#django-messages").text().trim() !== "") {
        $("#django-messages").removeClass("d-none");
        $("#toggleMessagesBtn").prop("disabled", false);
    }
});
