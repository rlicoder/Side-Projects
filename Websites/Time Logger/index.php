<!DOCTYPE html>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->
<html>
	<head>
		<meta charset="UTF-8">
		<link href="site.css" rel="stylesheet" type="text/css"/>
		<script src="loginhandler.js"></script>
		<title>Royce's Epic Time Logger</title>
	</head>
	<body>
		<header>
			<img src="header.png">
		</header>

		<div id="main" class="flex-container">
			<input type="button" class="button" value="Login" onclick="showLoginForm();"/>
			<input type="button" class="button" value ="Sign Up" onclick="showSignUpForm();"/>
		</div>

		<div id="loginForm">
			<form name="loginForm">
				<label for="loginUsername">Username</label>
				<input type="text" id="loginUsername"/>
				<label for="loginPassword">Password</label>
				<input type="password" id="loginPassword"/>
				<input type="button" id="loginSubmit" value="Login" onclick="test()"/>
			</form>
		</div>

		<div id="signUpForm">
			<form name="signUpForm">
				<label for="signUpUsername">Username</label>
				<input type="text" id="signUpUsername"/>
				<label for="signUpPassword">Password</label>
				<input type="password" id="signUpPassword"/>
				<label for="passwordConfirm">Confirm Password</label>
				<input type="password" id="passwordConfirm"/>
				<input type="button" id="signUpSubmit" value="Sign Up" onclick="test2()"/>
			</form>
		</div>
	</body>
</html>
