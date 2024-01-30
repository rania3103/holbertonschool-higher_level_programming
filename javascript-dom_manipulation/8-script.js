const url = fetch('https://hellosalut.stefanbohacek.dev/?lang=fr').then(res =>{
    return res.json();
}).then(data =>{
    const hello = document.getElementById('hello');
    hello.textContent = data.hello;
    
});
