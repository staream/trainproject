function func_color(){
    let element = document.querySelectorAll("h2");
    for (e of element){
        e.style.color='blue';
        e.innerText = e.innerText.toUpperCase();
    }
    
}

