document.getElementById('toggle_header').onclick = ()=>{
    const classAttr = document.querySelector('header').getAttribute('class');
    const header = document.querySelector('header');
    if (classAttr === 'red'){
        header.setAttribute('class','green');
    }else{
        header.setAttribute('class','red');
    }
}