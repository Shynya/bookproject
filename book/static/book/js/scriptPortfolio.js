/*let select = document.querySelector('[name="answers"]');*/

/*select.onchange = event => {
    console.log(select.selectedIndex);

}*/

var answers = document.getElementById('id_answers');
answers.addEventListener('change', (event) => {
    var selectanswers = document.getElementById('selectanswers')
    /*selectanswers.textContent = answers.options[answers.selectedIndex].value + ":" + answers.options[answers.selectedIndex].textContent; */
    
    /*var answersWidth = window.document.getElementById("id_answers").style.width*/
    /*selectanswers.textContent  = answers.options[answers.selectedIndex].textContent.length;*/
    if (selectanswers.textContent  <= 11) {
        /*answersWidth = "100px";*/
        /*document.getElementById("id_answers").setAttribute('width', '100px');*/
        /*answers.style.width = '100px';*/
        answers.style.fontSize = '16px';
    }else if (selectanswers.textContent  <= 16){
        answers.style.fontSize = '12px';
    }
    else{
        answers.style.fontSize = '50%';
    }
});

