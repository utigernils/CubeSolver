document.addEventListener("DOMContentLoaded", function() {

    eel.expose(UserInfo);
    function UserInfo(msg){
        alert(msg);
    }

    eel.expose(UpdateText);

    function UpdateText(object, value){
        var object = document.getElementById(object);
        object.innerHTML = value;
    }

    const AutostartOn_btn = document.getElementById("AutostartOn");
    const AutostartOff_btn = document.getElementById("AutostartOff");
    const Solve_btn = document.getElementById("Solve");
    const SelfTest_btn = document.getElementById("SelfTest");
    const Calibration_btn = document.getElementById("Calibration");

    AutostartOn_btn.addEventListener("click", function() {
        eel.home_AutostartOn_btn();
    });

    AutostartOff_btn.addEventListener("click", function() {
        eel.home_AutostartOff_btn();
    });

    Solve_btn.addEventListener("click", function() {
        eel.home_Solve_btn();
    });

    SelfTest_btn.addEventListener("click", function() {
        eel.home_SelfTest_btn();
    });

    Calibration_btn.addEventListener("click", function() {
        eel.home_Calibration_btn();
    });

    eel.home_loaded();
});