let select = document.querySelector('[name="shoseki"]');

let categoryAuto = document.getElementById("id_category");
let shosekiAuto = document.getElementById("id_shoseki");

select.onchange = event => { 
  // console.log(select.selectedIndex);
  if(select.value == 'Python3エンジニア認定基礎試験問題集' || select.value == 'Python3エンジニア認定基礎試験Web問題') {
        let categoryAutoText = 'Python3エンジニア認定基礎試験';
        categoryAuto.value = categoryAutoText;
    }else if(select.value == 'キタミ式ITイラスト塾　応用情報技術者　令和03年' || select.value == '令和04年【春期】　応用情報技術者　過去問題集' || select.value == '応用情報技術者　試験によくでる問題集【午後】'){
        let categoryAutoText = 'AP';
        categoryAuto.value = categoryAutoText;
    }else if(select.value == 'データベーススペシャリスト教科書令和4年度'){
        let categoryAutoText = 'DATABASE SPECIALIST';
        categoryAuto.value = categoryAutoText;
    }else if(select.value == 'Python3エンジニア認定データ分析試験Web問題'){
        let categoryAutoText = 'Python3エンジニア認定データ分析試験';
        categoryAuto.value = categoryAutoText;
    }else if(select.value == 'ディープラーニングG検定ジェネラリスト要点整理テキスト&問題集'){
        let categoryAutoText = 'G検定';
        categoryAuto.value = categoryAutoText;
    }else if(select.value == 'LINUC教科書LINUCレベル1スピードマスター問題集 VERSION10.0対応'){
        let categoryAutoText = 'LinuC1';
        categoryAuto.value = categoryAutoText;
    }else if(select.value == 'LPICレベル1スピードマスター問題集'){
        let categoryAutoText = 'LPIC1';
        categoryAuto.value = categoryAutoText;
    }else if(select.value == '統計検定2級　模擬問題集1' || select.value == '統計検定2級　模擬問題集2' || select.value == '統計検定2級　模擬問題集3'){
        let categoryAutoText = '統計検定2級';
        categoryAuto.value = categoryAutoText;
    }else if(select.value == 'Bronze 12c SQL 基礎問題集'){
        let categoryAutoText = 'Bronze 12c SQL基礎';
        categoryAuto.value = categoryAutoText;
    }else if(select.value == 'Python3エンジニア認定実践試験Web問題'){
        let categoryAutoText = 'Python3エンジニア認定実践試験';
        categoryAuto.value = categoryAutoText;
    }else if(select.value == 'シェルワンライナー100本ノック'){
        let categoryAutoText = 'Linux';
        categoryAuto.value = categoryAutoText;
    }else if(select.value == 'Excel VBA スタンダード'){
        let categoryAutoText = 'Excel VBA';
        categoryAuto.value = categoryAutoText;
    }else if(select.value == '基本情報技術者らくらく突破 Python'){
        let categoryAutoText = 'FE';
        categoryAuto.value = categoryAutoText;
    }else if(select.value == 'キタミ式ITイラスト塾　基本情報技術者　令和02年'){
        let categoryAutoText = 'FE';
        categoryAuto.value = categoryAutoText;
    }else if(select.value == '情報セキュリティマネジメント教科書令和2年度'){
        let categoryAutoText = '情報セキュリティマネジメント';
        categoryAuto.value = categoryAutoText;
    }else if(select.value == 'Access VBA スタンダード'){
        let categoryAutoText = 'Access VBA';
        categoryAuto.value = categoryAutoText;
    }else if(select.value == '徹底攻略データサイエンティスト検定リテラシーレベル問題集'){
        let categoryAutoText = 'データ　サイエンティスト';
        categoryAuto.value = categoryAutoText;
    }else if(select.value == '徹底攻略ディープラーニングE資格エンジニア問題集'){
        let categoryAutoText = 'ディープラーニングE資格';
        categoryAuto.value = categoryAutoText;
    }
    /*else{
        categoryAuto.value = '';
    }*/
    

}
let select2 = document.querySelector('[name="thumbnailQ1"]');
select2.onchange = event => { 
    /*最初非表示から表示 */  
    if(select2.value != ''){
        document.querySelector('.yokonarabi p:nth-child(4)').style.display = "block";
        
    };
}
let select22= document.querySelector('[name="thumbnailQ2"]');
select22.onchange = event => { 
    /*最初非表示から表示 */  
    if(select22.value != ''){
        document.querySelector('.yokonarabi p:nth-child(5)').style.display = "block";
        
    };
}
let select3 = document.querySelector('[name="wronganswer3"]');
select3.onchange = event => { 
    /*最初非表示から表示 */  
    if(select3.value != ''){
        document.querySelector('.yokonarabi p:nth-child(10)').style.display = "block";
        
    };
}
let select4 = document.querySelector('[name="wronganswer4"]');
select4.onchange = event => { 
    /*最初非表示から表示 */  
    if(select4.value != ''){
        document.querySelector('.yokonarabi p:nth-child(11)').style.display = "block";
        
    };
}
let select5 = document.querySelector('[name="wronganswer5"]');
select5.onchange = event => { 
    /*最初非表示から表示 */  
    if(select5.value != ''){
        document.querySelector('.yokonarabi p:nth-child(12)').style.display = "block";
        
    };
}
let select6 = document.querySelector('[name="wronganswer6"]');
select6.onchange = event => { 
    /*最初非表示から表示 */  
    if(select6.value != ''){
        document.querySelector('.yokonarabi p:nth-child(13)').style.display = "block";
        
    };
}
let select7 = document.querySelector('[name="wronganswer7"]');
select7.onchange = event => { 
    /*最初非表示から表示 */  
    if(select7.value != ''){
        document.querySelector('.yokonarabi p:nth-child(14)').style.display = "block";
        
    };
}
let select8 = document.querySelector('[name="wronganswer8"]');
select8.onchange = event => { 
    /*最初非表示から表示 */  
    if(select8.value != ''){
        document.querySelector('.yokonarabi p:nth-child(15)').style.display = "block";
        
    };
}
let select9 = document.querySelector('[name="wronganswer9"]');
select9.onchange = event => { 
    /*最初非表示から表示 */  
    if(select9.value != ''){
        document.querySelector('.yokonarabi p:nth-child(16)').style.display = "block";
        
    };
}
let select10 = document.querySelector('[name="hint1"]');
select10.onchange = event => { 
    /*最初非表示から表示 */  
    if(select10.value != ''){
        document.querySelector('.yokonarabi p:nth-child(17)').style.display = "block";
        
    };
}
let select23 = document.querySelector('[name="thumbnailA1"]');
select23.onchange = event => { 
    /*最初非表示から表示 */  
    if(select23.value != ''){
        document.querySelector('.yokonarabi p:nth-child(23)').style.display = "block";
        
    };
}
let select24 = document.querySelector('[name="thumbnailA2"]');
select24.onchange = event => { 
    /*最初非表示から表示 */  
    if(select24.value != ''){
        document.querySelector('.yokonarabi p:nth-child(24)').style.display = "block";
        
    };
}

    