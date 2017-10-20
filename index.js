function log() {
	if(loginbt.value == 'Login') {
		if(email.value =='') return;
		var logdata = {
			email : email.value,
			password : pass.value
		}
		$.post("login.cgi", logdata, function (data, status) {
			replace.innerHTML = data;   		 		
			if (data != "log in failed\n") {//\n!!!!!
				$("input").attr('readonly', true);
				loginbt.value ='Logout';
				signin.value = 'sell item';
				link.href = 'upload.html';
			}
		} );
	} else {
		$("input").attr('readonly', false);
		loginbt.value ='Login';
		email.value = '';
		pass.value = '';
		link.href = 'signin.html';
		signin.value = 'signin';
		replace.innerHTML = '';
	}
}

function search() {
	alert(search-text.value);
	var jv = { "search" : search-text.value };
	$.post("search.cgi", jv, fucntion(data, status) {
		replace.innerHTML = data;
	});
}

