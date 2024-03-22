document.addEventListener("DOMContentLoaded", function () {
  const MotorCom_select = document.getElementById("MotorCom");
  const MachineCom_select = document.getElementById("MachineCom");
  const CheckRate_select = document.getElementById("CheckRate");
  const Save_btn = document.getElementById("Save");

  //output
  MotorCom_select.addEventListener("change", function () {
    const value = MotorCom_select.value;
    eel.settings_MotorCom_select(value);
  });

  MachineCom_select.addEventListener("change", function () {
    const value = MachineCom_select.value;
    eel.settings_MachineCom_select(value);
  });

  CheckRate_select.addEventListener("change", function () {
    const value = CheckRate_select.value;
    eel.settings_CheckRate_select(value);
  });

  Save_btn.addEventListener("click", function () {
    eel.settings_Save_btn();
  });

  //input
  eel.expose(set_settings_MotorCom_select);
  function set_settings_MotorCom_select(value) {
    MotorCom_select.value = value;
  }

  eel.expose(set_settings_MachineCom_select);
  function set_settings_MachineCom_select(value) {
    MachineCom_select.value = value;
  }

  eel.expose(set_settings_CheckRate_select);
  function set_settings_CheckRate_select(value) {
    CheckRate_select.value = value;
  }

  eel.settings_loaded();
});
