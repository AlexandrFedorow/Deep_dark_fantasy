
    //Функция отображения PopUp
function PopUpShow(){
    $("#popup1").show();
}
    //Функция скрытия PopUp
function PopUpHide(){
    check_device_number();
    $("#popup1").hide();
}
PopUpHide();

function check_device_number(){
    s_number = document.getElementById('s-number').value;
    //тут где-то должна быть проверка формы через python
    //проверка на заполненност и на соответствие бд
    console.log(s_number);
}

function create_device(){
  //походу запускать эту функцию придеся через python
}
