const getInfoButton = document.querySelector('.get-info-button');
const errContainer = document.getElementById('errors-container');
const table = document.getElementById('contact-info-body');

getInfoButton.addEventListener('click', async () => {
    id = document.getElementById('contract-num-input').value;
    getInfoRequest(id);
})

async function getInfoRequest(id) {
    const response = await fetch(`http://localhost:5000/contract/${id}`);
    if (response.ok) {
        let data = await response.json();
        addToTable(data);
    } else {
        let error = `<h6 class="error">Не удалось получить данные по указанному номеру договора</h6>`;

        table.innerHTML = '';
        errContainer.innerHTML = error;
    }
}

function addToTable(data) {
    const info = `<tr>
    <td>${data.id}</td>
    <td>${data.name}</td>
    <td>${data.tariff}</td>
    <td>${data.status == true ? 'Активен' : 'Не активен'}</td>
    <td>${data.city}</td>
    <td>${data.street}</td>
    <td>${data.house}</td>
    <td>${data.apartment}</td>
</tr>`;

    errContainer.innerHTML = '';
    table.innerHTML = info;
}