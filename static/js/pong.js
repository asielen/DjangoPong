function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}

$(document).ready(function() {
    $("#id_player_1A").select2();
	$("#id_player_1B").select2();
	$("#id_player_2A").select2();
	$("#id_player_2B").select2();
});


/* SELECT2 Functions */
$( "#swapTeam1" ).click(function() {
  	var player1A = $("[name=player_1A]").children("option:selected").val();
	var player1B = $("[name=player_1B]").children("option:selected").val();
	$("[name=player_1A]").select2("val", 0);
	$("[name=player_1B]").select2("val", 0);
	$("[name=player_1A]").select2("val", player1B); //SELECT2
	$("[name=player_1B]").select2("val", player1A); //SELECT2
});

$( "#swapTeam2" ).click(function() {
	var player2A = $("[name=player_2A]").children("option:selected").val();
	var player2B = $("[name=player_2B]").children("option:selected").val();
	$("[name=player_2A]").select2("val", 0);
	$("[name=player_2B]").select2("val", 0);
	$("[name=player_2A]").select2("val", player2B); //SELECT2
	$("[name=player_2B]").select2("val", player2A); //SELECT2
});

$( "#shuffle" ).click(function() {
	let players = [];
	players.push($("[name=player_1A]").children("option:selected").val());
	players.push($("[name=player_1B]").children("option:selected").val());
	players.push($("[name=player_2A]").children("option:selected").val());
	players.push($("[name=player_2B]").children("option:selected").val());

	shuffleArray(players);

	// filter out nulls
	players = players.filter(Boolean);
	// Null out all players
	$("[name=player_1A]").select2("val", 0);
	$("[name=player_1B]").select2("val", 0);
	$("[name=player_2A]").select2("val", 0);
	$("[name=player_2B]").select2("val", 0);

	$("[name=player_1A]").select2("val", players[0]); //SELECT2
	$("[name=player_2A]").select2("val", players[1]); //SELECT2

	if (players.length>=3) {
		if (Math.random() >= 0.5) {
			$("[name=player_1B]").select2("val", players[2]); //SELECT2
			if (players.length==4) {
				$("[name=player_2B]").select2("val", players[3]); //SELECT2
			}
		} else {
			$("[name=player_2B]").select2("val", players[2]); //SELECT2
			if (players.length==4) {
				$("[name=player_1B]").select2("val", players[3]); //SELECT2
			}
		}

	}

});


$( "#rotate" ).click(function() {
	let players = [];
	players.push($("[name=player_1A]").children("option:selected").val());
	players.push($("[name=player_1B]").children("option:selected").val());
	players.push($("[name=player_2A]").children("option:selected").val());
	players.push($("[name=player_2B]").children("option:selected").val());

	// Null out all players
	$("[name=player_1A]").select2("val", 0);
	$("[name=player_1B]").select2("val", 0);
	$("[name=player_2A]").select2("val", 0);
	$("[name=player_2B]").select2("val", 0);

	if(players.filter(Boolean).length==2) {
		players = players.filter(Boolean);

		$("[name=player_1A]").select2("val", players[1]); //SELECT2
		$("[name=player_2A]").select2("val", players[0]); //SELECT2
	} else {
		if (players[3]==0) {
			// if there is no new 1A
			$("[name=player_1A]").select2("val", players[0]); //SELECT2
		} else {

			$("[name=player_1A]").select2("val", players[3]); //SELECT2
			$("[name=player_1B]").select2("val", players[0]); //SELECT2
		}
		if (players[1]==0) {
			$("[name=player_2A]").select2("val", players[2]); //SELECT2
		} else {

			$("[name=player_2A]").select2("val", players[1]); //SELECT2
			$("[name=player_2B]").select2("val", players[2]); //SELECT2
		}



	}
});

$( "#swap" ).click(function() {
	// 0,1,2,3  0,1   3,2
	// 3,2,1,0  3,2   0,1
	// TODO: Swap fails with 2 people when they are both Bs
	let players = [];
	players.push($("[name=player_1A]").children("option:selected").val());
	players.push($("[name=player_1B]").children("option:selected").val());
	players.push($("[name=player_2A]").children("option:selected").val());
	players.push($("[name=player_2B]").children("option:selected").val());

	// Null out all players
	$("[name=player_1A]").select2("val", 0);
	$("[name=player_1B]").select2("val", 0);
	$("[name=player_2A]").select2("val", 0);
	$("[name=player_2B]").select2("val", 0);


	if(players.filter(Boolean).length==2) {

		$("[name=player_1A]").select2("val", players[2]); //SELECT2
		$("[name=player_2A]").select2("val", players[0]); //SELECT2
	} else {
		if (players[2]==0) {
			// if there is no new 1A
			$("[name=player_1A]").select2("val", players[3]); //SELECT2
		} else {
			$("[name=player_1A]").select2("val", players[2]); //SELECT2
			$("[name=player_1B]").select2("val", players[3]); //SELECT2
		}
		if (players[0]==0) {
			$("[name=player_2A]").select2("val", players[1]); //SELECT2
		} else {
			$("[name=player_2A]").select2("val", players[0]); //SELECT2
			$("[name=player_2B]").select2("val", players[1]); //SELECT2
		}
	}
});

var windowteam = 1;
$( "#swapwindow" ).click(function() {
	if (windowteam == 1) {
		$("#wall").css("background-color", "lightblue");
		$("#window").css("background-color", "beige");
		$("#window #weather").css("display", "none");
		$("#wall #weather").css("display", "initial");
		windowteam = 2
	} else {
		$("#wall").css("background-color", "beige");
		$("#window").css("background-color", "lightblue");
		$("#window #weather").css("display", "initial");
		$("#wall #weather").css("display", "none");
		windowteam = 1
	}
	$("#id_window_team").val(windowteam);
	// console.log("New Window Team ",windowteam);
});

$( "#upTeam1" ).click(function() {
	$("#id_team_1_Score").val(parseInt($("#id_team_1_Score").val())+1)
});
$( "#downTeam1" ).click(function() {
	$("#id_team_1_Score").val(Math.max(parseInt($("#id_team_1_Score").val())-1,0))
});
$( "#upTeam2" ).click(function() {
	$("#id_team_2_Score").val(parseInt($("#id_team_2_Score").val())+1)
});
$( "#downTeam2" ).click(function() {
	$("#id_team_2_Score").val(Math.max(parseInt($("#id_team_2_Score").val())-1,0))
});

$('input').on('click', function(){
	ga('send', 'event', 'Interface', 'Click', this.id, '0');
});

/* No SELECT 2
$( "#swapTeam1" ).click(function() {
  	var player1A = $("[name=player_1A]").children("option:selected").val();
	var player1B = $("[name=player_1B]").children("option:selected").val();
	$("[name=player_1A]").children("option:selected").prop('selected', false);
	$("[name=player_1B]").children("option:selected").prop('selected', false);
	$("[name=player_1A] option[value='"+player1B+"']").prop('selected', true);
	$("[name=player_1B] option[value='"+player1A+"']").prop('selected', true);
	$("[name=player_1A]").select2("val", player1B); //SELECT2
	$("[name=player_1B]").select2("val", player1A); //SELECT2
});

$( "#swapTeam2" ).click(function() {
	var player2A = $("[name=player_2A]").children("option:selected").val();
	var player2B = $("[name=player_2B]").children("option:selected").val();
	$("[name=player_2A]").children("option:selected").prop('selected', false);
	$("[name=player_2B]").children("option:selected").prop('selected', false);
	$("[name=player_2A] option[value='"+player2B+"']").prop('selected', true);
	$("[name=player_2B] option[value='"+player2A+"']").prop('selected', true);
	$("[name=player_2A]").select2("val", player2B); //SELECT2
	$("[name=player_2B]").select2("val", player2A); //SELECT2
});

$( "#shuffle" ).click(function() {
	let players = [];
	players.push($("[name=player_1A]").children("option:selected").val());
	players.push($("[name=player_1B]").children("option:selected").val());
	players.push($("[name=player_2A]").children("option:selected").val());
	players.push($("[name=player_2B]").children("option:selected").val());

	shuffleArray(players);

	// filter out nulls
	players = players.filter(Boolean);
	// Null out all players
	$("[name=player_1A]").children("option:selected").prop('selected', false);
	$("[name=player_1B]").children("option:selected").prop('selected', false);
	$("[name=player_2A]").children("option:selected").prop('selected', false);
	$("[name=player_2B]").children("option:selected").prop('selected', false);

	$("[name=player_1A]").select2("val", players[0]); //SELECT2
	$("[name=player_2A]").select2("val", players[1]); //SELECT2

	$("[name=player_1A] option[value='"+players[0]+"']").prop('selected', true);
	$("[name=player_2A] option[value='"+players[1]+"']").prop('selected', true);
	if (players.length>=3) {
		if (Math.random() >= 0.5) {
			$("[name=player_1B]").select2("val", players[2]); //SELECT2
			$("[name=player_1B] option[value='"+players[2]+"']").prop('selected', true);
			if (players.length==4) {
				$("[name=player_2B]").select2("val", players[3]); //SELECT2
				$("[name=player_2B] option[value='"+players[3]+"']").prop('selected', true);
			}
		} else {
			$("[name=player_2B]").select2("val", players[2]); //SELECT2
			$("[name=player_2B] option[value='"+players[2]+"']").prop('selected', true);
			if (players.length==4) {
				$("[name=player_1B]").select2("val", players[3]); //SELECT2
				$("[name=player_1B] option[value='"+players[3]+"']").prop('selected', true);
			}
		}

	}

});


$( "#rotate" ).click(function() {
	let players = [];
	players.push($("[name=player_1A]").children("option:selected").val());
	players.push($("[name=player_1B]").children("option:selected").val());
	players.push($("[name=player_2A]").children("option:selected").val());
	players.push($("[name=player_2B]").children("option:selected").val());

	// Null out all players
	$("[name=player_1A]").children("option:selected").prop('selected', false);
	$("[name=player_1B]").children("option:selected").prop('selected', false);
	$("[name=player_2A]").children("option:selected").prop('selected', false);
	$("[name=player_2B]").children("option:selected").prop('selected', false);

	if(players.filter(Boolean).length==2) {
		players = players.filter(Boolean);
		$("[name=player_1A] option[value='"+players[1]+"']").prop('selected', true);
		$("[name=player_2A] option[value='"+players[0]+"']").prop('selected', true);

		$("[name=player_1A]").select2("val", players[1]); //SELECT2
		$("[name=player_2A]").select2("val", players[0]); //SELECT2
	} else {
		if (players[3]=="") {
			// if there is no new 1A
			$("[name=player_1A] option[value='"+players[0]+"']").prop('selected', true);
			$("[name=player_1A]").select2("val", players[0]); //SELECT2
		} else {
			$("[name=player_1A] option[value='"+players[3]+"']").prop('selected', true);
			$("[name=player_1B] option[value='"+players[0]+"']").prop('selected', true);

			$("[name=player_1A]").select2("val", players[3]); //SELECT2
			$("[name=player_1B]").select2("val", players[0]); //SELECT2
		}
		if (players[1]=="") {
			$("[name=player_2A] option[value='"+players[2]+"']").prop('selected', true);

			$("[name=player_2A]").select2("val", players[2]); //SELECT2
		} else {
			$("[name=player_2A] option[value='"+players[1]+"']").prop('selected', true);
			$("[name=player_2B] option[value='"+players[2]+"']").prop('selected', true);

			$("[name=player_2A]").select2("val", players[1]); //SELECT2
			$("[name=player_2B]").select2("val", players[2]); //SELECT2
		}



	}
});

$( "#swap" ).click(function() {
	// 0,1,2,3  0,1   3,2
	// 3,2,1,0  3,2   0,1
	let players = [];
	players.push($("[name=player_1A]").children("option:selected").val());
	players.push($("[name=player_1B]").children("option:selected").val());
	players.push($("[name=player_2A]").children("option:selected").val());
	players.push($("[name=player_2B]").children("option:selected").val());

	// Null out all players
	$("[name=player_1A]").children("option:selected").prop('selected', false);
	$("[name=player_1B]").children("option:selected").prop('selected', false);
	$("[name=player_2A]").children("option:selected").prop('selected', false);
	$("[name=player_2B]").children("option:selected").prop('selected', false);

	$("[name=player_1A]").select2("val", "");
	$("[name=player_1B]").select2("val", "");
	$("[name=player_2A]").select2("val", "");
	$("[name=player_2B]").select2("val", "");


	if(players.filter(Boolean).length==2) {
		$("[name=player_1A] option[value='"+players[2]+"']").prop('selected', true);
		$("[name=player_2A] option[value='"+players[0]+"']").prop('selected', true);

		$("[name=player_1A]").select2("val", players[2]); //SELECT2
		$("[name=player_2A]").select2("val", players[0]); //SELECT2
	} else {
		if (players[2]=="") {
			// if there is no new 1A
			$("[name=player_1A] option[value='"+players[3]+"']").prop('selected', true);

			$("[name=player_1A]").select2("val", players[3]); //SELECT2
		} else {
			$("[name=player_1A] option[value='"+players[2]+"']").prop('selected', true);
			$("[name=player_1B] option[value='"+players[3]+"']").prop('selected', true);

			$("[name=player_1A]").select2("val", players[2]); //SELECT2
			$("[name=player_1B]").select2("val", players[3]); //SELECT2
		}
		if (players[0]=="") {
			$("[name=player_2A] option[value='"+players[1]+"']").prop('selected', true);
			$("[name=player_2A]").select2("val", players[1]); //SELECT2
		} else {
			$("[name=player_2A] option[value='"+players[0]+"']").prop('selected', true);
			$("[name=player_2B] option[value='"+players[1]+"']").prop('selected', true);
			$("[name=player_2A]").select2("val", players[0]); //SELECT2
			$("[name=player_2B]").select2("val", players[1]); //SELECT2
		}



	}
});
*/