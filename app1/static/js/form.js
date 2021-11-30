// appoinment is ready
$(document).ready(function () {

	// Validate fristname
	$('#firstcheck').hide();
	let firstnameError = true;
	$('#firstnames').keyup(function () {
		validatefirstname();
	});

	function validatefirstname() {
		let firstnameValue = $('#firstnames').val();
		if (firstnameValue.length == '') {
			$('#firstcheck').show();
			firstnameError = false;
			return false;
		}
		else if ((firstnameValue.length < 3) ||
			(firstnameValue.length > 20)) {
			$('#firstcheck').show();
			$('#firstcheck').html
				("**length of firstname must be between 3 and 10");
			firstnameError = false;
			return false;
		}
		else {
			$('#firstcheck').hide();
		}
	}

	// Validate lastname
	$('#lastcheck').hide();
	let lastnameError = true;
	$('#lastnames').keyup(function () {
		validatelastname();
	});

	function validatelastname() {
		let lastnameValue = $('#lastnames').val();
		if (lastnameValue.length == '') {
			$('#lastcheck').show();
			lastnameError = false;
			return false;
		}
		else if ((lastnameValue.length < 3) ||
			(lastnameValue.length > 20)) {
			$('#lastcheck').show();
			$('#lastcheck').html
				("**length of lastname must be between 3 and 10");
			lastnameError = false;
			return false;
		}
		else {
			$('#lastcheck').hide();
		}
	}

	// Validate Email
	const email =
		document.getElementById('email');
	email.addEventListener('blur', () => {
		let regex =
			/^([_\-\.0-9a-zA-Z]+)@([_\-\.0-9a-zA-Z]+)\.([a-zA-Z]){2,7}$/;
		let s = email.value;
		if (regex.test(s)) {
			email.classList.remove(
				'is-invalid');
			emailError = true;
		}
		else {
			email.classList.add(
				'is-invalid');
			emailError = false;
		}
	})

	// Validate Password
	$('#passcheck').hide();
	let passwordError = true;
	$('#password').keyup(function () {
		validatePassword();
	});
	function validatePassword() {
		let passwrdValue =
			$('#password').val();
		if (passwrdValue.length == '') {
			$('#passcheck').show();
			passwordError = false;
			return false;
		}
		if ((passwrdValue.length < 3) ||
			(passwrdValue.length > 15)) {
			$('#passcheck').show();
			$('#passcheck').html
				("**length of your password must be between 3 and 10");
			$('#passcheck').css("color", "red");
			passwordError = false;
			return false;
		} else {
			$('#passcheck').hide();
		}
	}

	// Validate Confirm Password
	$('#conpasscheck').hide();
	let confirmPasswordError = true;
	$('#conpassword').keyup(function () {
		validateConfirmPasswrd();
	});
	function validateConfirmPasswrd() {
		let confirmPasswordValue =
			$('#conpassword').val();
		let passwrdValue =
			$('#password').val();
		if (passwrdValue != confirmPasswordValue) {
			$('#conpasscheck').show();
			$('#conpasscheck').html(
				"**Password didn't Match");
			$('#conpasscheck').css(
				"color", "red");
			confirmPasswordError = false;
			return false;
		} else {
			$('#conpasscheck').hide();
		}
	}

	// Submit button
	$('#submitbtn').click(function () {
		validatefirstname();
		validatelastname();
		validatePassword();
		validateConfirmPasswrd();
		validateEmail();
		if ((firstnameError == true) &&
			(lastnameError == true) &&
			(passwordError == true) &&
			(confirmPasswordError == true) &&
			(emailError == true)) {
			return true;
		} else {
			return false;
		}
	});
});






// signup form is ready


$(document).ready(function () {

	// Validate fristname
	$('#firstcheck2').hide();
	let firstname2Error = true;
	$('#firstnames2').keyup(function () {
		validatefirstname2();
	});

	function validatefirstname2() {
		let firstname2Value = $('#firstnames2').val();
		if (firstname2Value.length == '') {
			$('#firstcheck2').show();
			firstname2Error = false;
			return false;
		}
		else if ((firstname2Value.length < 3) ||
			(firstname2Value.length > 20)) {
			$('#firstcheck2').show();
			$('#firstcheck2').html
				("**length of firstname must be between 3 and 10");
			firstname2Error = false;
			return false;
		}
		else {
			$('#firstcheck2').hide();
		}
	}



	// Validate Email
	const email2 =
		document.getElementById('email2');
	email2.addEventListener('blur', () => {
		let regex =
			/^([_\-\.0-9a-zA-Z]+)@([_\-\.0-9a-zA-Z]+)\.([a-zA-Z]){2,7}$/;
		let s = email2.value;
		if (regex.test(s)) {
			email2.classList.remove(
				'is-invalid');
			email2Error = true;
		}
		else {
			email2.classList.add(
				'is-invalid');
			email2Error = false;
		}
	})

	// Validate Password
	$('#passcheck2').hide();
	let password2Error = true;
	$('#password2').keyup(function () {
		validatePassword2();
	});
	function validatePassword2() {
		let passwrd2Value =
			$('#password2').val();
		if (passwrd2Value.length == '') {
			$('#passcheck2').show();
			password2Error = false;
			return false;
		}
		if ((passwrd2Value.length < 3) ||
			(passwrd2Value.length > 20)) {
			$('#passcheck2').show();
			$('#passcheck2').html
				("**length of your password must be between 3 and 15");
			$('#passcheck2').css("color", "red");
			password2Error = false;
			return false;
		} else {
			$('#passcheck2').hide();
		}
	}

	// Validate Confirm Password
	$('#conpasscheck2').hide();
	let confirmPassword2Error = true;
	$('#conpassword2').keyup(function () {
		validateConfirmPasswrd2();
	});
	function validateConfirmPasswrd2() {
		let confirmPassword2Value =
			$('#conpassword2').val();
		let passwrd2Value =
			$('#password2').val();
		if (passwrd2Value != confirmPassword2Value) {
			$('#conpasscheck2').show();
			$('#conpasscheck2').html(
				"**Password didn't Match");
			$('#conpasscheck2').css(
				"color", "red");
			confirmPassword2Error = false;
			return false;
		} else {
			$('#conpasscheck2').hide();
		}
	}

	// Submit button
	$('#submitbtn2').click(function () {
		validatefirstname2();
		validatePassword2();
		validateConfirmPasswrd2();
		validateEmail2();
		if ((firstname2Error == true) &&
			(password2Error == true) &&
			(confirmPassword2Error == true) &&
			(email2Error == true)) {
			return true;
		} else {
			return false;
		}
	});
});
