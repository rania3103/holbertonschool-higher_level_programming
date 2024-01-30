document.getElementById('add_item').onclick = ()=>{
    const ulElement = document.querySelector('.my_list');
    const newUl = document.createElement('li');
    newUl.textContent = 'Item';
    ulElement.appendChild(newUl);
};