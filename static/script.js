const getInfoButton = document.querySelector('.get-info__button');

getInfoButton.addEventListener('click', async () => {
    fetch('http://localhost:5000/balance/1')
        .then(data => data.text())
        .then(data => {
            console.log(data)
        })
    // await getInfoRequest();
})

function getInfoRequest() {
    return fetch('http://localhost:5000/balance/1')
        .then(data => data.text())
        .then(data => {
            console.log(data)
        })
}

function showContractInfo(posts) {

}