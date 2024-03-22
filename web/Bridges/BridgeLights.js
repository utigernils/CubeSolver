document.addEventListener("DOMContentLoaded", function() {

    const ResetIdle_btn = document.getElementById("ResetIdle");
    const SetIdle_btn = document.getElementById("SetIdle");
    const ResetScanning_btn = document.getElementById("ResetScanning");
    const SetScanning_btn = document.getElementById("SetScanning");
    const ResetSolving_btn = document.getElementById("ResetSolving");
    const SetSolving_btn = document.getElementById("SetSolving");
    const ResetDone_btn = document.getElementById("ResetDone");
    const SetDone_btn = document.getElementById("SetDone");

    ResetIdle_btn.addEventListener("click", function() {
        eel.lights_ResetIdle_btn();
    });

    SetIdle_btn.addEventListener("click", function() {
        eel.lights_SetIdle_btn();
    });

    ResetScanning_btn.addEventListener("click", function() {
        eel.lights_ResetScanning_btn();
    });

    SetScanning_btn.addEventListener("click", function() {
        eel.lights_SetScanning_btn();
    });

    ResetSolving_btn.addEventListener("click", function() {
        eel.lights_ResetSolving_btn();
    });

    SetSolving_btn.addEventListener("click", function() {
        eel.lights_SetSolving_btn();
    });

    ResetDone_btn.addEventListener("click", function() {
        eel.lights_ResetDone_btn();
    });

    SetDone_btn.addEventListener("click", function() {
        eel.lights_SetDone_btn();
    });

    const AnimationIdle_select = document.getElementById("AnimationIdle");
    const AnimationScanning_select = document.getElementById("AnimationScanning");
    const AnimationSolving_select = document.getElementById("AnimationSolving");
    const AnimationDone_select = document.getElementById("AnimationDone");

    AnimationIdle_select.addEventListener("change", function() {
        const value = AnimationIdle_select.value;
        eel.lights_AnimationIdle_select(value);
    });

    AnimationScanning_select.addEventListener("change", function() {
        const value = AnimationScanning_select.value;
        eel.lights_AnimationScanning_select(value);
    });

    AnimationSolving_select.addEventListener("change", function() {
        const value = AnimationSolving_select.value;
        eel.lights_AnimationSolving_select(value);
    });

    AnimationDone_select.addEventListener("change", function() {
        const value = AnimationDone_select.value;
        eel.lights_AnimationDone_select(value);
    });

    const ColorIdle_color = document.getElementById("ColorIdle");
    const ColorScanning_color = document.getElementById("ColorScanning");
    const ColorSolve_color = document.getElementById("ColorSolve");
    const ColorDone_color = document.getElementById("ColorDone");

    ColorIdle_color.addEventListener("change", function() {
        const value = ColorIdle_color.value;
        eel.lights_ColorIdle_color(value);
    });

    ColorScanning_color.addEventListener("change", function() {
        const value = ColorScanning_color.value;
        eel.lights_ColorScanning_color(value);
    });

    ColorSolve_color.addEventListener("change", function() {
        const value = ColorSolve_color.value;
        eel.lights_ColorSolve_color(value);
    });

    ColorDone_color.addEventListener("change", function() {
        const value = ColorDone_color.value;
        eel.lights_ColorDone_color(value);
    });

    eel.expose(set_lights_AnimationIdle_select);
    function set_lights_AnimationIdle_select(value) {
        AnimationIdle_select.value = value;
    }

    eel.expose(set_lights_AnimationScanning_select);
    function set_lights_AnimationScanning_select(value) {
        AnimationScanning_select.value = value;
    }

    eel.expose(set_lights_AnimationSolving_select);
    function set_lights_AnimationSolving_select(value) {
        AnimationSolving_select.value = value;
    }

    eel.expose(set_lights_AnimationDone_select);
    function set_lights_AnimationDone_select(value) {
        AnimationDone_select.value = value;
    }

    eel.expose(set_lights_ColorIdle_color);
    function set_lights_ColorIdle_color(value) {
        ColorIdle_color.value = value;
        document.querySelector('#ColorIdle').dispatchEvent(new Event('input', { bubbles: true }));
    }

    eel.expose(set_lights_ColorScanning_color);
    function set_lights_ColorScanning_color(value) {
        ColorScanning_color.value = value;
        document.querySelector('#ColorScanning').dispatchEvent(new Event('input', { bubbles: true }));
    }

    eel.expose(set_lights_ColorSolving_color);
    function set_lights_ColorSolving_color(value) {
        ColorSolve_color.value = value;
        document.querySelector('#ColorSolve').dispatchEvent(new Event('input', { bubbles: true }));
    }

    eel.expose(set_lights_ColorDone_color);
    function set_lights_ColorDone_color(value) {
        ColorDone_color.value = value;
        document.querySelector('#ColorDone').dispatchEvent(new Event('input', { bubbles: true }));
    }

    eel.lights_loaded();

});
