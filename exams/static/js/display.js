const url = window.location.href
console.log(url)

const examBox = document.getElementById('exam-box')
let data

//The following will get the data required to display the available exams

$.ajax({
    type: 'GET',
    url: `${url}data`,
    success: function(response){
        console.log(response)
        data = response.data
        data.forEach(el => {
            for (const [question, answers] of Object.entries(el)){
                console.log(question)
                console.log(answers)
            }
        })
    },
    error: function(error){
        console.log(error)
    }
})