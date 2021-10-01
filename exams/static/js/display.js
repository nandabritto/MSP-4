const url = window.location.href
console.log(url)

const examBox = document.getElementById('exam-box')
const scoreDisplay = document.getElementById('scoredisplay')
const resultDisplay = document.getElementById('resultdisplay')
const timerDisplay = document.getElementById('timerDisplay')



// Activating the countdown timer
const activateTimer = (time) => {
    console.log(time)

    if (time.toString().length < 2) {
        timerDisplay.innerHTML = `<b>0${time}:00</b>`
    } else {
        timerDisplay.innerHTML = `<b>0${time}:00</b>`
    }

    let minutes = time -1
    console.log(minutes)
}



//The following will get the data required to display the available exams

$.ajax({
    type: 'GET',
    url: `${url}data`,
    success: function(response){
        let data = response.data
        console.log(data)
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
        
        
    },
    error: function(error){
        console.log(error)
    }
})

const examForm = document.getElementById('exam-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

// The following code will display the results
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
        url:`${url}save/`,
        data: data,
        success: function(response){
            const results = response.results
            console.log(results)
            examForm.classList.add('not-visible')

            scoreBox.innerHTML = `${response.passed ? 'Congratulations! ' : 'Oops... Not this time'} Your result is ${response.score}%`

            results.forEach(res=>{
                const resDiv = document.createElement("div")
                for (const [question, resp] of Object.entries(res)){

                    resDiv.innerHTML += question
                    const cls = ['container', 'p-3', 'text-light', 'h3']
                    resDiv.classList.add(...cls)

                    // if no response recieved - red
                    if (resp=='not answered') {
                        resDiv.innerHTML += '- not answered'
                        resDive.classList.add('bg-danger')
                    }
                    // if response received
                    else {
                        const answer = resp['answered']
                        const correct = resp['correct answer']
                        console.log(answer, correct)
                        // if the answer is correct
                        if (answer == correct) {
                            resDiv.classList.add('bg-success')
                            resDiv.innerHTML += `answered: ${answer}`
                        // if the answer was incorrect
                        } else {
                            resDiv.classList.add('bg-danger')
                            resDiv.innerHTML += ` | correct answer: ${correct}`
                            resDiv.innerHTML += ` | answered: ${answer}`
                        }
                    }
                }
                // const body = document.getElementsByTagName('BODY')[0]
                resultDisplay.append(resDiv)
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
