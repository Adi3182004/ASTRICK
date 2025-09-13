$(document).ready(function () {

    // Display Speak Message
    eel.expose(DisplayMessage)
    function DisplayMessage(message) {
        $(".siri-message li:first").text(message);
        $('.siri-message').textillate('start');
    }

    // Display hood
    eel.expose(ShowHood)
    function ShowHood() {
        $("#Oval").attr("hidden", false);
        $("#SiriWave").attr("hidden", true);
    }

    eel.expose(senderText)
    function senderText(message) {
        var chatBox = document.getElementById("chat-canvas-body");
        if (message.trim() !== "") {
            chatBox.innerHTML += `<div class="row justify-content-end mb-4">
                <div class = "width-size">
                    <div class="sender_message">${message}</div>
                </div>
            </div>`; 
    
            // Scroll to the bottom of the chat box
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    }

    eel.expose(receiverText)
    function receiverText(message) {
        var chatBox = document.getElementById("chat-canvas-body");
        if (message.trim() !== "") {
            chatBox.innerHTML += `<div class="row justify-content-start mb-4">
                <div class = "width-size">
                    <div class="receiver_message">${message}</div>
                </div>
            </div>`; 
    
            // Scroll to the bottom of the chat box
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    }

    // Hide Loader and display Face Auth animation
    eel.expose(hideloader)
    function hideloader() {
        $("#loader").attr("hidden", true);
        $("#FaceAuth").attr("hidden", false);
    }

    // Hide Face auth and display Face Auth success animation
    eel.expose(hideFaceAuth)
    function hideFaceAuth() {
        $("#FaceAuth").attr("hidden", true);
        $("#FaceAuthSuccess").attr("hidden", false);
    }

    // Hide success and display
    eel.expose(hideFaceAuthSuccess)
    function hideFaceAuthSuccess() {
        $("#FaceAuthSuccess").attr("hidden", true);
        $("#HelloGreet").attr("hidden", false);
    }

    // Hide Start Page and display blob
    eel.expose(hideStart)
    function hideStart() {
        $("#Start").attr("hidden", true);

        setTimeout(function () {
            $("#Oval").addClass("animate__animated animate__zoomIn");
        }, 1000);

        setTimeout(function () {
            $("#Oval").attr("hidden", false);
        }, 1000);
    }

    // Display Recognized Text
    eel.expose(DisplayRecognizedText);
    function DisplayRecognizedText(message) {
        console.log("Received message from backend:", message); // Debug log
        const siriMessage = document.querySelector(".siri-message");
        if (siriMessage) {
            siriMessage.textContent = message; // Replace the existing text
            $('.siri-message').textillate('start'); // Optional animation
        } else {
            console.error("Siri message element not found!");
        }
    }

});
