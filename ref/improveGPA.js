//keep track of if submission is valid
var valid = true;

function getName() {
    //get name
    var name = document.getElementById("name").value;
    var pattern = /[^a-zA-Z\s]/i;

    //check input against pattern
    //if empty do this
    if (document.getElementById("name").value == "") {
        document.getElementById("nameErr").innerHTML = "*This field is required";
        valid = false;
    }

    //if invalid character detected do this
    else if (name.match(pattern) != null) {
        document.getElementById("nameErr").innerHTML = "Only letters and whitespace allowed";
        valid = false;
    }

    //else correct
    else {
        document.getElementById("nameErr").innerHTML = "";
        valid = true;
    }
}

function getEmail() {
    
    //validation formula from stack overflow page https://stackoverflow.com/questions/46155/how-to-validate-an-email-address-in-javascript
    var email = document.getElementById("email").value;
    var pattern = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

    //check it against the pattern
    //if correct do this
    if (pattern.test(String(email)) == true) {
        document.getElementById("emailErr").innerHTML = "";
    }

    //if empty do this
    else if (document.getElementById("email").value == "") {
        document.getElementById("emailErr").innerHTML = "*This field is required";
        valid = false;
    }

    //if improper format do this
    else {
        document.getElementById("emailErr").innerHTML = "Invalid E-mail Format";
        valid = false;
    }
}

function getCheckbox() {
    //get checkbox
    var check = document.getElementById("agree").checked;

    //if checked
    if (check) {
        document.getElementById("agreeErr").innerHTML = "";
    }

    //if not checked
    else {
        document.getElementById("agreeErr").innerHTML = "*You must agree with the terms and conditions";
        valid = false;
    }
}

function getCurrGpa() {
    //get the current gpa
    var cGpa = document.getElementById("currentGPA").value;

    //check if in range
    //if outside of range
    if (cGpa < 0 || cGpa > 4) {
        document.getElementById("currentGPAErr").innerHTML = "*Sorry your input is out of range";
        valid = false;
    }

    //if empty
    else if (cGpa == "") {
        document.getElementById("currentGPAErr").innerHTML = "*This field is required";
        valid = false;
    }

    //if correct
    else {
        document.getElementById("currentGPAErr").innerHTML = "";
        return cGpa;
    }
}

function getCurrTotalCreds() {
    //get current credits
    var cCreds = document.getElementById("currentCredits").value;

    //check to see if in range
    if (cCreds < 0) {
        document.getElementById("currentCreditsErr").innerHTML = "*Sorry your input is out of range";
        valid = false;
    }

    //if empty
    else if (cCreds == "") {
        document.getElementById("currentCreditsErr").innerHTML = "*This field is required";
        valid = false;
    }

    //if correct
    else {
        document.getElementById("currentCreditsErr").innerHTML = "";
        return cCreds;
    }
}

function getNewCreds() {
    //check the new creds being taken
    var nCreds = document.getElementById("newCredits").value;

    // if empty
    if (nCreds == "") {
        document.getElementById("newCreditsErr").innerHTML = "*This field is required";
        valid = false;
    }

    //if outside of range
    else if (nCreds <= 0) {
        document.getElementById("newCreditsErr").innerHTML = "*Sorry your input is out of range";
        valid = false;
    }

    //if correct
    else {
        document.getElementById("newCreditsErr").innerHTML = "";
        return nCreds;
    }
}

function getGpaInc() {
    //get the desired gpaincrease
    var gpaInc = document.getElementById("GPAincrease").value;

    //if empty
    if (gpaInc == "") {
        document.getElementById("GPAincreaseErr").innerHTML = "*This field is required";
        valid = false;
    }

    //if outside of range
    else if (gpaInc < 0) {
        document.getElementById("GPAincreaseErr").innerHTML = "*Sorry your input is out of range";
        valid = false;
    }

    //if correct
    else {
        document.getElementById("GPAincreaseErr").innerHTML = "";
        return gpaInc;
    }
}

function processForm() {
    //get all the input from the form
    getName();
    getEmail();
    getCheckbox();

    /*store the ones with useful data in variables for calculations
      parse out the numbers for each
    */

    //curent gpa
    var cgpa = parseFloat(getCurrGpa());

    //current credits
    var ccred = parseInt(getCurrTotalCreds());

    //new credits being taken
    var ncreds = parseInt(getNewCreds());

    //desired increase in gpa
    var gpainc = parseFloat(getGpaInc());

    //if successful submission
    console.log(valid);
    if (valid) {
        //current gpa hours
        var cgpahours = parseFloat(cgpa) * parseFloat(ccred);

        //desired gpa
        var dgpa = parseFloat(cgpa) + parseFloat(gpainc);

        //desired gpa hours
        var dgpahours = parseFloat((dgpa * (ccred + ncreds)));

        //the increase in gpa
        var gpahoursinc = parseFloat(dgpahours - cgpahours);

        //gpa required to meet goal
        var ngpa = parseFloat(gpahoursinc / ncreds);

        //print outcome
        document.getElementById("amount").innerHTML = ngpa;
    }

    //on unsuccessful submisssion
    else {
        document.getElementById("amount").innerHTML = "????";
        valid = false;
    }
}