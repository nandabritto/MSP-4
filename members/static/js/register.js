// Updating the Member Registration fields
var form_fields = document.getElementsByClassName('form-control')
form_fields[1].placeholder='Username..';
form_fields[2].placeholder='Email..';
form_fields[3].placeholder='Enter password...';
form_fields[4].placeholder='Re-enter Password...';


for (var field in form_fields){	
    form_fields[field].className += 'form-control'
}