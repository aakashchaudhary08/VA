$(document).ready(function () {

    eel.expose(DisplayMessage);
    function DisplayMessage(message) {

        // stop animation
        $('.siri-message').textillate('stop');

        // update text
        $(".siri-message li:first").text(message);

        // restart animation
        $('.siri-message').textillate('start');

    }

    eel.expose(ShowHood);
    function ShowHood() {

        $("#Oval").attr("hidden", false);
        $("#SiriWave").attr("hidden", true);

        // reset message so next command works
        $(".siri-message li:first").text("Click mic and speak...");

    }

});