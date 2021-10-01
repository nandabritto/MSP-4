const url = window.location.href

const examBox = document.getElementById('exam-box')
const scoreBox = document.getElementById('score-box')
const resultBox = document.getElementById('result-box')
const timerBox = document.getElementById('timer-box')


// activating the countdown timer
const activateTimer = (time) => {
    if (time.toString().length < 2) {
        timerBox.innerHTML = `<b>0${time}:00</b>`
    } else {
        timerBox.innerHTML = `<b>${time}:00</b>`
    }

    let minutes = time - 1
    let seconds = 60
    let displaySeconds
    let displayMinutes

    const timer = setInterval(()=>{
        seconds --
        if (seconds < 0) {
            seconds = 59
            minutes --
        }
        if (minutes.toString().length < 2) {
            displayMinutes = '0'+minutes
        } else {
            displayMinutes = minutes
        }
        if(seconds.toString().length < 2) {
            displaySeconds = '0' + seconds
        } else {
            displaySeconds = seconds
        }
        // handles timeout and auto send at 0:00
        if (minutes === 0 && seconds === 0) {
            timerBox.innerHTML = "<b>00:00</b>"
            setTimeout(()=>{
                clearInterval(timer)
                alert('Time over')
                sendData()
            }, 500)
        }

        timerBox.innerHTML = `<b>${displayMinutes}:${displaySeconds}</b>`
    }, 1000)
}

// The following code will get and display the required data for the chosen exam
$.ajax({
    type: 'GET',
    url: `${url}data`,
    success: function(response){
        const data = response.data
        data.forEach(el => {
            for (const [question, answers] of Object.entries(el)){
                examBox.innerHTML += `
                    <hr>
                    <div class="mb-2">
                        <b>${question}</b>
                    </div>
                `
                answers.forEach(answer=>{
                    examBox.innerHTML += `
                        <div>
                            <input type="radio" class="ans" id="${question}-${answer}" name="${question}" value="${answer}">
                            <label for="${question}">${answer}</label>
                        </div>
                    `
                })
            }
        });
        activateTimer(response.time)
        
    },
    error: function(error){
        console.log(error)
    }
})

const examForm = document.getElementById('exam-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')


//The following code will display the results

const sendData = () => {
    const data = {}
    data['csrfmiddlewaretoken'] = csrf[0].value
    const elements = [...document.getElementsByClassName('ans')]
    elements.forEach(el=>{
        if (el.checked) {
            //compares the question to the answer
            data[el.name] = el.value
        } else {
            //checks if answer was not given by user
            if (!data[el.name]) {
                data[el.name] = null
            }
        }

    })

    $.ajax({
        type: 'POST',
        url: `${url}save/`,
        data: data,
        success: function(response){
            const results = response.results
            console.log(results)
            examForm.classList.add('not-visible')

            scoreBox.innerHTML = `${response.passed ? 'Congratulations! ' : 'Oops..:( '}Your result is ${response.score.toFixed(2)}%`

            results.forEach(res=>{
                const resDiv = document.createElement("div")
                for (const [question, resp] of Object.entries(res)){

                    resDiv.innerHTML += question
                    const cls = ['container', 'p-3', 'text-light', 'h6']
                    resDiv.classList.add(...cls)

                    // if no repose received - red
                    if (resp=='not answered') {
                        resDiv.innerHTML += `<div class="alert alert-warning" role="alert">
                        <h4 class="alert-heading">You didn't respond</h4>
                        <p> "Nothing" is not the correct answer for ${question} </p>
                        <p> Back to the books for you</p>
                      </div>`
                    }
                    // if response received
                    else {
                        const answer = resp['answered']
                        const correct = resp['correct_answer']
                        console.log(answer, correct)
                        // If the answer was correct
                        if (answer == correct) {
                            resDiv.innerHTML += `<div class="alert alert-success" role="alert">
                            <h4 class="alert-heading">Well Done</h4>
                            <p> You are correct, the answer to ${question} </p>
                            <p> is :${answer}</p>
                          </div>`
                        // If the answer was incorrect
                        } else {
                            resDiv.innerHTML += `<div class="alert alert-danger" role="alert">
                            <h4 class="alert-heading">Not this time</h4>
                            <p> That's not the correct answer for ${question} </p>
                            <p> The correct answer is :${answer}</p>
                          </div>`
                        }
                    }
                }
                resultBox.append(resDiv)
            })
        },
        error: function(error){
            console.log(error)
        }
    })
}


examForm.addEventListener('submit', e=>{
    e.preventDefault()

    sendData()
})