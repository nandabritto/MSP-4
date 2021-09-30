const modalTitle = document.getElementById('exampleModalLabel')
const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementsById('modal-body-confirm')
const startBtn = document.getElementsById('start-button')

const url = window.location.href

modalBtns.forEach(modalBtn=> modalBtn.addEventListener('click', ()=>{
    const pk = modalBtn.getAttribute('data-pk')
    const name = modalBtn.getAttribute('data-exam')
    const numQuestions = modalBtn.getAttribute('data-questions')
    const difficulty = modalBtn.getAttribute('data-difficulty')
    const scoreToPass = modalBtn.getAttribute('data-pass')
    const time = modalBtn.getAttribute('data-time')

    modalTitle.innerHTML = `<b>${name}</b>`

    modalBody.innerHTML = `
        <div class="h5 mb-3">Are you sure you want to begin?</div>
        <div class="text-muted">
            <ul>
                <li>Difficulty: <b>${difficulty}</b></li>
                <li>No of Questions: <b>${numQuestions}</b></li>
                <li>Score to Pass: <b>${scoreToPass}</b></li>
                <li>Time: <b>${time} min</b></li>
            </ul>
        </div>
    `

    startBtn.addEventListener('click', ()=>{
        window.location.href = url + pk
    })
}))