// Toggle the visibility of the messages div
function toggleMessages() {
    $('#django-messages').toggle();
}

// Show messages div only when there are messages
$(document).ready(function () {
    if ($('#django-messages p').length > 0) {
        $('#django-messages').removeClass('hidden');
        $('#toggleMessagesBtn').prop('disabled', false);
    }
});