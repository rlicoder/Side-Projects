function showLoginForm()
{
    document.getElementById("loginForm").style.display = "block";
    document.getElementById("signUpForm").style.display = "none";
}

function showSignUpForm()
{
    document.getElementById("signUpForm").style.display = "block";
    document.getElementById("loginForm").style.display = "none";
}

function test()
{
    var username = document.forms["loginForm"]["loginUsername"].value;
    var password = document.forms["loginForm"]["loginPassword"].value;
    alert(username + " " + password);
}

function test2()
{
    var username = document.forms["signUpForm"]["signUpUsername"].value;
    var password = document.forms["signUpForm"]["signUpPassword"].value;
    var passwordc = document.forms["signUpForm"]["passwordConfirm"].value;
    //if (password !== passwordc)
    //{
    //
    //}
    alert(username + " " + password + " " + passwordc);
}