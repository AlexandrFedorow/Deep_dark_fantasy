
var ctr = -1; // счетчик отвечает за количесто блоков
var device_name = '';



function PopUpShow(){ //Функция отображения PopUp
    $("#popup1").show();
}


    //Функция скрытия PopUp
async function PopUpHide(){
    if (ctr > -1){
        var s_number = document.getElementById('s-number').value;
        device_name = document.getElementById('name').value;
        var check = await eel.call(s_number)();

        if (check == 1){
            create_device();
        }
        else{
          alert('пососи')  // НЕ ЗАБУДЬ УБРАТЬ
          ctr--;
        }
    }
    ctr++;

    $("#popup1").hide();
}

function PopUpExit(){
    $("#popup1").hide();
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

  var text = document.createTextNode(device_name);

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
  div5.id = ctr+'light';
  div.id = ctr;
  div.setAttribute('onclick', 'choose_devace(this)')
  main.appendChild(div);
  main.appendChild(br);
}


function choose_devace(obj){//эта функция для отображения информации о дивайсе
  refresh();
  for(var i = 0; i<4; i++){
    var b = document.getElementById('plot'+i);
    b.style.opacity = 1;
  }
  var a = document.getElementById(obj.id+'t');
  var b = document.getElementById('l2');

  var textA = a.innerHTML;
  b.innerHTML = textA;

  var plot0 = document.getElementById('plot0');
  var plot1 = document.getElementById('plot1');
  var plot2 = document.getElementById('plot2');
  var plot3 = document.getElementById('plot3');

  if(ctr != -1){
    plot0.src = "static/plot0.png";
    plot1.src = "static/plot2.png";
    plot2.src = "static/plot1.png";
    plot3.src = "static/plot2.png";
  }
}

async function refresh(){
    var plot0 = document.getElementById('plot0');
    var plot1 = document.getElementById('plot1');
    var plot2 = document.getElementById('plot2');
    var plot3 = document.getElementById('plot3');

    if(ctr != 0){
      var a = await eel.get_data()();
      plot0.src = "static/plot0.png";
      plot1.src = "static/plot1.png";
      plot2.src = "static/plot2.png";
      plot3.src = "static/plot3.png";
    }
}



PopUpHide();
