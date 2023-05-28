const searchForm = document.querySelector('#search-form');
const searchResults = document.querySelector('#search-results');
const PortfolioSearch = document.querySelector('#PortfolioDiv');


searchForm.addEventListener('submit', function (e) {
    e.preventDefault(); // предотвращаем перезагрузку страницы
    const formData = new FormData(searchForm); // получаем данные формы

    // формируем URL с параметрами запроса
    const urlParams = new URLSearchParams(formData);

    let cleanLink = searchForm.action.replace(/#.*$/, "");

    const url = `${cleanLink}?${urlParams}`;

    // отправляем AJAX-запрос на сервер
    fetch(url)
        .then(response => response.text())
        .then(html => {
            const parser = new DOMParser();
            const doc = parser.parseFromString(html, "text/html");
            const PortfolioDiv = doc.querySelector("#search-results"); // выбираем элемент по ID
            const PortfolioDivmini = doc.querySelector("#PortfolioDiv"); // выбираем элемент по ID
            searchResults.innerHTML = PortfolioDiv.innerHTML;
            PortfolioSearch.innerHTML = PortfolioDivmini.innerHTML;
        })
        .catch(error => console.error(error));

});


// const searchForm = document.querySelector('#search-form');
// const searchResults = document.querySelector('#search-results');
// const PortfolioSearch = document.querySelector('#PortfolioDiv');
//
// searchForm.addEventListener('submit', function (e) {
//     e.preventDefault(); // предотвращаем перезагрузку страницы
//     const formData = new FormData(searchForm); // получаем данные формы
//
//     // формируем URL с параметрами запроса
//     const urlParams = new URLSearchParams(formData);
//     const url = `${searchForm.getAttribute('action')}?${urlParams}${location.hash}`;
//
//     // отправляем AJAX-запрос на сервер
//     fetch(url)
//         .then(response => response.text())
//         .then(html => {
//             const parser = new DOMParser();
//             const doc = parser.parseFromString(html, "text/html");
//             const PortfolioDiv = doc.querySelector("#search-results"); // выбираем элемент по ID
//             const PortfolioDivmini = doc.querySelector("#PortfolioDiv"); // выбираем элемент по ID
//             searchResults.innerHTML = PortfolioDiv.innerHTML;
//             PortfolioSearch.innerHTML = PortfolioDivmini.innerHTML;
//         })
//         .catch(error => console.error(error));
//
// });
