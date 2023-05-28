function showDiv() {
    // Отключаем прокрутку на основной странице
    document.body.style.overflow = "hidden";
    // Отображаем див
    document.getElementById("PortfolioDiv").style.display = "flex";
    // Включаем прокрутку внутри дива
    document.getElementById("PortfolioDiv").style.overflow = "auto";

}


function hideDiv() {
    // Включаем прокрутку на основной странице
    document.body.style.overflow = "auto";
    // Скрываем див
    document.getElementById("PortfolioDiv").style.display = "none";
}
function showContact() {
    // Отключаем прокрутку на основной странице
    document.body.style.overflow = "hidden";
    // Отображаем див
    document.getElementById("ContactForm").style.display = "flex";
    // Включаем прокрутку внутри дива
    document.getElementById("ContactForm").style.overflow = "auto";

}


function hideContact() {
    // Включаем прокрутку на основной странице
    document.body.style.overflow = "auto";
    // Скрываем див
    document.getElementById("ContactForm").style.display = "none";
}



