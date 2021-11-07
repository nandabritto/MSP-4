// setting the window url for use in the ajax queries
const url = window.location.href

// Setting the const for the html elements to be updated
const examBox = document.getElementById('exam-box')
const scoreDisplay = document.getElementById('scoredisplay')
const resultDisplay = document.getElementById('resultsdisplay')
const timerBox = document.getElementById('timerdisplay')
const endButton = document.getElementById('endbutton')
let timer;

// Setting up the timer which counts down based on each individual exam limit
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
    timer = setInterval(()=>{
        seconds --
        if (seconds < 0) {
            seconds = 59
            minutes --
        }
        if (minutes.toString().length < 2) {
            displayMinutes = '0'+ minutes
        } else {
            displayMinutes = minutes
        }
        if(seconds.toString().length < 2) {
            displaySeconds = '0' + seconds
        } else {
            displaySeconds = seconds
        }
        if (minutes === 0 && seconds === 0) {
            setTimeout(()=>{
                clearInterval(timer)
                alert('Time over')
                sendData()
            }, 500)
        }
        // Actual countdown display
        timerBox.innerHTML = `
            <div>
                <b>${displayMinutes}:${displaySeconds}</b>
            </div>`
    }, 1000)
}

// Automatically obtains the exam questions/answers on page load
$.ajax({
    type: 'GET',
    url: `${url}data`,
    success: function(response){
        const data = response.data
        data.forEach(el => {
            for (const [question, answers] of Object.entries(el)){
                // Populates the question being asked
                examBox.innerHTML += `
                    <hr>
                    <div class="container"
                        <div class="row pl-5">
                            <h5><b>Question: ${question}</b></h5>
                        </div>
                    </div>
                `
                // Populates the answers which are matched to the previously chosen question
                answers.forEach(answer=>{
                    examBox.innerHTML += `
                    <div class="container">
                        <div class="pl-5">
                            <input type="radio" class="ans" id="${question}-${answer}" name="${question}" value="${answer}">
                            <label for="${question}">${answer}</label>
                        </div>
                    </div>
                `
                })
            }
        });
        // Activates the countdown timer once the questions have loaded
        activateTimer(response.time)
        
    },
    error: function(error){
        console.log(error)
    }
})

const examForm = document.getElementById('exam-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

// Gets the Users answers and holds them to be compared with the correct answers in the DB
const sendData = () => {
    const elements = [...document.getElementsByClassName('ans')]
    const data = {}
    data['csrfmiddlewaretoken'] = csrf[0].value
    elements.forEach(el=>{
        if (el.checked) {
            data[el.name] = el.value
        } else {
            if (!data[el.name]) {
                data[el.name] = null
            }
        }
    })

    // Functions to provide the "grading" of the submitted answers
    $.ajax({
        type: 'POST',
        url: `${url}save`,
        data: data,
        success: function(response){
            clearInterval(timer);
            // Populates the reset and back to exam list buttons once answers have been submitted
            endButton.innerHTML += `
                <hr>
                <div class="container"
                    <div class="row pl-5">
                        <a href="{% url 'index' %}" class="btn btn-danger">Go Back</a>
                        <button class="btn btn-success float-right" onClick="window.location.reload();">Try Again</button>
                    </div>
                </div>
                `
            const results = response.results
            // Once answers have been submitted, timer and questions will disappear
            examForm.classList.add('not-visible')
            timerBox.classList.add('not-visible')

            // prints out the overall score results
            scoreDisplay.innerHTML = `${response.passed ? 'Congratulations! ' : 'Oops..:( '}Your result is ${response.score.toFixed(2)}%`

            // The below will populate the results for each question
            results.forEach(res=>{
                const resDiv = document.createElement("div")
                for (const [question, resp] of Object.entries(res)){

                    // if no repose received - Correct answer is not displayed
                    if (resp=='not answered') {
                        resDiv.innerHTML += `
                        <div class="row justify-content-center">
                            <div class="col-9">
                                <div class="alert alert-warning" role="alert">
                                <h4 class="alert-heading">You didn't respond</h4>
                                <p> "Nothing" is not the correct answer for <b>${question}</b> </p>
                                <p> Back to the books for you</p>
                                </div>
                            </div>
                        </div>`
                    }
                    // if response received
                    else {
                        const answer = resp['answered']
                        const correct = resp['correct_answer']
                        // If the answer received was correct
                        if (answer == correct) {
                            resDiv.innerHTML += `
                            <div class="row justify-content-center">
                                <div class="col-9">
                                    <div class="alert alert-success" role="alert">
                                        <h4 class="alert-heading">Well Done</h4>
                                        <p> You are correct, the answer to <b>${question}</b></p>
                                        <p> is: <b>${answer}</b></p>
                                    </div>
                                </div>
                          </div>`
                        // If the answer received was incorrect
                        } else {
                            resDiv.innerHTML += `
                            <div class="row justify-content-center">
                                <div class="col-9">
                                    <div class="alert alert-danger" role="alert">
                                        <h4 class="alert-heading">Not this time</h4>
                                        <p><b>${answer}</b> is not the correct answer for <b>${question}</b> </p>
                                        <p> The correct answer is : <b>${correct}</b></p>
                                    </div>
                                </div>
                            </div>`
                        }
                    }
                }
                // Collates all question/answer results to single print
                resultDisplay.append(resDiv)
            })
        },
        error: function(error){
            console.log(error)
        }
    })
}

// Triggers the results event based on mouse click of Submit button
examForm.addEventListener('submit', e=>{
    e.preventDefault()
    sendData()
})