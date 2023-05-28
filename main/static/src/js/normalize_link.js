const form = document.querySelector('#search-form');
form.addEventListener('submit', function (e) {
    e.preventDefault();
    const formData = new FormData(form);
    const params = new URLSearchParams(formData);
    const searchParams = new URLSearchParams(params.toString());
    searchParams.forEach(function (value, key) {
        if (value === '') {
            params.delete(key);
        }
    });
    const url = `${form.action}?${params}`;
    window.location.href = url;
});
