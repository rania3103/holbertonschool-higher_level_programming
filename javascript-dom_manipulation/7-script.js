const url = fetch('https://swapi-api.hbtn.io/api/films/?format=json').then(res =>{
    return res.json();
}).then(data =>{
    const listMovies = document.getElementById('list_movies');
    data.results.forEach(element => {
        const lItem = document.createElement('li');
        lItem.textContent = element.title;
        listMovies.appendChild(lItem);
    });
})
