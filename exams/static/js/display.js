const url = window.location.href
console.log(url)

//The following will get the data required to display the available exams

$.ajax({
    type: 'GET',
    url: `${url}data`,
    success: function(response){
        console.log(response)
    },
    error: function(error){
        console.log(error)
    }
})