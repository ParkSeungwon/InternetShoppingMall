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
				signin.value = 'sell item';
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
	var v = $("#search-text").val();
	var jv = { search : v };
	$.post("search.cgi", jv, function(data, status) {
		var dat = data.split("$$separator$$");
		alert(data);
		var i=0;
		var lines = '';
		while(i<dat.length) {
			lines += "<tr><td><img height=250 width=250 src='image/" + dat[i++] + "'></td>";
			for(j=1; j<4; j++) lines += '<td>' + dat[i++] + '</td>';
			lines += '</tr>'
		}
		$("#goods").html(lines);
	});
}

