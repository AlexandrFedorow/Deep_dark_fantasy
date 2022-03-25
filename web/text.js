
var ctr = 0; // счетчик отвечает за количесто блоков
    //Функция отображения PopUp
function PopUpShow(){
    $("#popup1").show();
}


    //Функция скрытия PopUp
function PopUpHide(){
    //check_device_number();
    if (ctr > 0){
        create_device();
    }
    ctr++;

    $("#popup1").hide();
}


function check_device_number(){
    s_number = document.getElementById('s-number').value;
    //тут где-то должна быть проверка формы через python
    //проверка на заполненност и на соответствие бд
    console.log(s_number);
}


function create_device(){//походу запускать эту функцию придеся через python
  var br = document.createElement('br');

  var main = document.querySelector('div.bok');
  var div = document.createElement('div');
  var div1 = document.createElement('div');
  var div2 = document.createElement('div');
  var table = document.createElement('table');
  var tr = document.createElement('tr');
  var td1 = document.createElement('td');
  var td2 = document.createElement('td');
  var td3 = document.createElement('td');

  var div3 = document.createElement('div');
  var div4 = document.createElement('div');
  var div5 = document.createElement('div');

  var text = document.createTextNode("jjj");

  div.appendChild(div1);
  div.appendChild(div2);
  div2.appendChild(table);
  table.appendChild(tr);
  tr.appendChild(td1);
  tr.appendChild(td2);
  tr.appendChild(td3);
  td1.appendChild(div3)
  td2.appendChild(div4)
  td3.appendChild(div5)
  div4.appendChild(text);
  //div2.appendChild(text);

  div.className = 'block';
  div1.className = 'cost2';
  div2.className = 'cost';
  div3.className = 'ico';
  div4.className = 'text';
  div5.className = 'light';
  div4.id = ctr+'t';
  div.id = ctr;
  div.setAttribute('onclick', 'choose_devace(this)')
  main.appendChild(div);
  main.appendChild(br);
}


async function bb(){
    await eel.call();
}

function choose_devace(obj){//эта функция для отображения информации о дивайсе
  var a = document.getElementById(obj.id+'t');
  var b = document.getElementById('l2');

  var textA = a.innerHTML;
  b.innerHTML = textA;
}

PopUpHide();
