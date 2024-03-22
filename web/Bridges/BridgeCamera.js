document.addEventListener("DOMContentLoaded", function () {
  const Reset_btn = document.getElementById("Reset");
  const Set_btn = document.getElementById("Set");
  const SwitchCamera_btn = document.getElementById("SwitchCamera");
  const Mask_select = document.getElementById("Mask");
  const UpperHue_slider = document.getElementById("UpperHue");
  const LowerHue_slider = document.getElementById("LowerHue");
  const UpperSaturation_slider = document.getElementById("UpperSaturation");
  const LowerSaturation_slider = document.getElementById("LowerSaturation");
  const UpperBrightness_slider = document.getElementById("UpperBrightness");
  const LowerBrightness_slider = document.getElementById("LowerBrightness");

  Reset_btn.addEventListener("click", function () {
    eel.camera_Reset_btn();
  });

  Set_btn.addEventListener("click", function () {
    eel.camera_Set_btn();
  });

  SwitchCamera_btn.addEventListener("click", function () {
    eel.camera_SwitchCamera_btn();
  });

  Mask_select.addEventListener("change", function (event) {
    const value = event.target.value;
    eel.camera_Mask_select(value);
  });

  UpperHue_slider.addEventListener("change", function (event) {
    const value = event.target.value;
    eel.camera_UpperHue_slider(value);
  });

  LowerHue_slider.addEventListener("change", function (event) {
    const value = event.target.value;
    eel.camera_LowerHue_slider(value);
  });

  UpperSaturation_slider.addEventListener("change", function (event) {
    const value = event.target.value;
    eel.camera_UpperSaturation_slider(value);
  });

  LowerSaturation_slider.addEventListener("change", function (event) {
    const value = event.target.value;
    eel.camera_LowerSaturation_slider(value);
  });

  UpperBrightness_slider.addEventListener("change", function (event) {
    const value = event.target.value;
    eel.camera_UpperBrightness_slider(value);
  });

  LowerBrightness_slider.addEventListener("change", function (event) {
    const value = event.target.value;
    eel.camera_LowerBrightness_slider(value);
  });

  eel.expose(set_camera_Mask_select);
  function set_camera_Mask_select(value) {
    Mask_select.value = value;
  }
  
  eel.expose(set_camera_UpperHue_slider);
  function set_camera_UpperHue_slider(value) {
    UpperHue_slider.value = value;
  }
  
  eel.expose(set_camera_LowerHue_slider);
  function set_camera_LowerHue_slider(value) {
    LowerHue_slider.value = value;
  }
  
  eel.expose(set_camera_UpperSaturation_slider);
  function set_camera_UpperSaturation_slider(value) {
    UpperSaturation_slider.value = value;
  }
  
  eel.expose(set_camera_LowerSaturation_slider);
  function set_camera_LowerSaturation_slider(value) {
    LowerSaturation_slider.value = value;
  }
  
  eel.expose(set_camera_UpperBrightness_slider);
  function set_camera_UpperBrightness_slider(value) {
    UpperBrightness_slider.value = value;
  }
  
  eel.expose(set_camera_LowerBrightness_slider);
  function set_camera_LowerBrightness_slider(value) {
    LowerBrightness_slider.value = value;
  }

  eel.expose(refresh_img);
  function refresh_img(img) {
    document.getElementById('cameraImage').src = img
  }

  eel.camera_loaded();
});
