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
				$("#log_panel").css('visibility', 'hidden');
				loginbt.value ='Logout';
				signin.value = 'donate item';
				link.href = 'upload.html';
			}
		} );
	} else {
		$("#log_panel").css('visibility', 'visible');
		loginbt.value ='Login';
		email.value = '';
		pass.value = '';
		link.href = 'signin.html';
		signin.value = 'signin';
		replace.innerHTML = '';
	}
}

function search() {
	var jv = { search : $("#search-text").val() };
	$.post("search.cgi", jv, function(data, status) {
		var dat = data.split("$$separator$$");
		var i=0;
		var lines = '';
		while(i<dat.length-1) {
			lines += "<tr><td><img height=250 width=250 src='image/" + dat[i++] + "'></td>";
			for(j=1; j<5; j++) lines += '<td>' + dat[i++] + '</td>';
			lines += '</tr>'
		}
		$("#goods").html(lines);
	});
}

