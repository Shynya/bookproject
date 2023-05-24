/* 入力中に一時的にフォームの高さが大きくなる*/

/* id_question */
// ▼①フォーカスを得た場合
function gotfocus() {
    this.style.height = "10em";             // 高さを10文字分にする
    this.style.backgroundColor = "#ffe";    // 背景色を薄い黄色にする
}

function gotfocus2() {
    this.style.height = "20em";             // 高さを20文字分にする
    this.style.backgroundColor = "#ffe";    // 背景色を薄い黄色にする
}

// ▼②フォーカスを失った場合
function lostfocus() {
    //if( this.value.length == 0 ) {
    if( this.value.length <= 50 ) {
        // 文字数がゼロなら
        this.style.height = "2em";          // 高さを3文字分にする
    }else if(this.value.length <= 50) {
        this.style.height = "3em"; 
    }else{
        this.style.height = "4em";
    }
    this.style.backgroundColor = "#fff";    // 背景色を白色にする
}
 
// ③テキストエリアのイベントに、上記関数を割り当てる
document.getElementById("id_question").onfocus = gotfocus;    // フォーカスを得た場合
document.getElementById("id_question").onblur = lostfocus;    // フォーカスを失った場合


/* id_explanation */
// ③テキストエリアのイベントに、上記関数を割り当てる
document.getElementById("id_explanation").onfocus = gotfocus2;    // フォーカスを得た場合
document.getElementById("id_explanation").onblur = lostfocus;    // フォーカスを失った場合


function twoOfFour() {
    wronganswer1 = document.getElementById("id_wronganswer1");
    wronganswer2 = document.getElementById("id_wronganswer2");
    wronganswer3 = document.getElementById("id_wronganswer3");
    wronganswer4 = document.getElementById("id_wronganswer4");
    wronganswer5 = document.getElementById("id_wronganswer5");
    wronganswer6 = document.getElementById("id_wronganswer6");
    /*text = document.getElementById("text");*/
    text = "A, A, A";
    /*answerText = text.value;*/
    wronganswer1Text = "A, B";
    wronganswer1.innerText = wronganswer1Text;

    wronganswer2Text = "A, C";
    wronganswer2.innerText = wronganswer2Text;

    wronganswer3Text = "A, D";
    wronganswer3.innerText = wronganswer3Text;

    wronganswer4Text = "B, C";
    wronganswer4.innerText = wronganswer4Text;

    wronganswer5Text = "B, D";
    wronganswer5.innerText = wronganswer5Text;

    wronganswer6Text = "C, D";
    wronganswer6.innerText = wronganswer6Text;
  }

function appearAuto() {
   
    categoryAuto = document.getElementById("id_category");
    shosekiAuto = document.getElementById("id_shoseki");
    
  
    if( shosekiAuto.innerText == 'Python3エンジニア認定基礎試験問題集' ) {
        categoryAutoText = 'Python3エンジニア認定基礎試験';
        categoryAuto.innerText = categoryAutoText;
        }
}