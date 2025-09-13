let isStopped = false;
let isSpeaking = false;

// Hide stop button and SiriWave on load
$(function () {
    $("#stopBtn").attr("hidden", true);
    $("#SiriWave").attr("hidden", true);
});

$(document).ready(function () {

    // ✅ Expose showChatAfterSpeech so Python can call it after speaking
    eel.expose(showChatAfterSpeech);
    function showChatAfterSpeech() {
        isSpeaking = false;
        isStopped = false;
        $("#SiriWave").attr("hidden", true);
        $("#Oval").attr("hidden", false);
        $("#stopBtn").attr("hidden", true);
    }

    // ✅ Expose startListening so Python can call eel.startListening()
    eel.expose(startListening);
    function startListening() {
        startSpeaking();          // Shows SiriWave, hides idle button
        eel.allCommands();        // Start voice recognition
    }

    // ✅ Expose playAssistantSound so Python can trigger start sound
    eel.expose(playAssistantSound);
    function playAssistantSound() {
        var audio = new Audio("assets/audio/start_sound.mp3");
        audio.play().catch(function (e) {
            console.warn("Autoplay blocked:", e);
        });
    }

    eel.init()();

    // Text animations
    $('.text').textillate({
        loop: false,
        in: {
            effect: "bounceIn",
            callback: function () {
                $('.text').textillate('stop');
            }
        }
    });

    $('.siri-message').textillate({
        loop: false,
        in: {
            effect: "None",
            callback: function () {
                $('.siri-message').textillate('stop');
            }
        }
    });

    // Mic button triggers speaking + command
    $("#MicBtn").click(function () {
        startSpeaking();
        eel.allCommands()();
    });

    // Keyboard shortcut (Cmd/Ctrl + J)
    function doc_keyUp(e) {
        if (e.key === 'j' && e.metaKey) {
            startSpeaking();
            eel.allCommands()();
        }
    }
    document.addEventListener('keyup', doc_keyUp, false);

    // Show SiriWave visualizer and stop button
    function startSpeaking() {
        isStopped = false;
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        $("#stopBtn").removeAttr("hidden");
    }

    // Stop speaking
    function stopSpeaking() {
        isStopped = true;
        isSpeaking = false;

        if ('speechSynthesis' in window) {
            window.speechSynthesis.cancel();
        }

        eel.forceStopTTS(); // Stop pyttsx3 speaking

        $("#SiriWave").attr("hidden", true);
        $("#Oval").attr("hidden", false);
        $("#stopBtn").attr("hidden", true);
    }

    // Expose for Python usage
    eel.expose(startSpeaking);
    eel.expose(stopSpeaking);

    // Manual stop
    $("#stopBtn").click(function () {
        stopSpeaking();
    });

    // Handle text input sending
    function PlayAssistant(message) {
        if (message !== "" && !isStopped) {
            startSpeaking();
            eel.allCommands(message);
            $("#chatbox").val("");
            $("#MicBtn").attr('hidden', false);
            $("#SendBtn").attr('hidden', true);
        }
    }

    function ShowHideButton(message) {
        if (message.length === 0) {
            $("#MicBtn").attr('hidden', false);
            $("#SendBtn").attr('hidden', true);
        } else {
            $("#MicBtn").attr('hidden', true);
            $("#SendBtn").attr('hidden', false);
        }
    }

    // Toggle mic/send button based on input
    $("#chatbox").keyup(function () {
        let message = $("#chatbox").val();
        ShowHideButton(message);
    });

    // Manual send button
    $("#SendBtn").click(function () {
        isStopped = false;
        let message = $("#chatbox").val();
        PlayAssistant(message);
    });

    // Press Enter to send
    $("#chatbox").keypress(function (e) {
        if (e.which === 13) {
            isStopped = false;
            let message = $("#chatbox").val();
            PlayAssistant(message);
        }
    });
});
