/* 入力中に一時的にフォームの高さが大きくなる*/

/* id_question */
// ▼①フォーカスを得た場合
function gotfocus() {
    this.style.height = "10em";             // 高さを10文字分にする
    this.style.backgroundColor = "#ffe";    // 背景色を薄い黄色にする
}

function gotfocus2() {
    this.style.height = "20em";             // 高さを10文字分にする
    this.style.backgroundColor = "#ffe";    // 背景色を薄い黄色にする
}

// ▼②フォーカスを失った場合
function lostfocus() {
    if( this.value.length == 0 ) {
        // 文字数がゼロなら
        this.style.height = "2em";          // 高さを3文字分にする
    }
    this.style.backgroundColor = "#fff";    // 背景色を白色にする
}
 
// ③テキストエリアのイベントに、上記関数を割り当てる
document.getElementById("id_titile").onfocus = gotfocus;    // フォーカスを得た場合
document.getElementById("id_title").onblur = lostfocus;    // フォーカスを失った場合

/* id_answer */
// ③テキストエリアのイベントに、上記関数を割り当てる
document.getElementById("id_text").onfocus = gotfocus;    // フォーカスを得た場合
document.getElementById("id_text").onblur = lostfocus;    // フォーカスを失った場合
