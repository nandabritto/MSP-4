const url = window.location.href
console.log(url)

const examBox = document.getElementById('exam-box')


//The following will get the data required to display the available exams

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
            console.log(response)
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
