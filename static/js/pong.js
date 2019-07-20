
$("#id_player_1A").chosen();
$("#id_player_1B").chosen();
$("#id_player_2A").chosen();
$("#id_player_2B").chosen();





function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}


$( "#swapTeam1" ).click(function() {
  var player1A = $("[name=player_1A]").children("option:selected").val();
	var player1B = $("[name=player_1B]").children("option:selected").val();
	$("[name=player_1A]").children("option:selected").prop('selected', false);
	$("[name=player_1B]").children("option:selected").prop('selected', false);
	$("[name=player_1A] option[value='"+player1B+"']").prop('selected', true);
	$("[name=player_1B] option[value='"+player1A+"']").prop('selected', true);
});

$( "#swapTeam2" ).click(function() {
  var player2A = $("[name=player_2A]").children("option:selected").val();
	var player2B = $("[name=player_2B]").children("option:selected").val();
	$("[name=player_2A]").children("option:selected").prop('selected', false);
$("[name=player_2B]").children("option:selected").prop('selected', false);
$("[name=player_2A] option[value='"+player2B+"']").prop('selected', true);
$("[name=player_2B] option[value='"+player2A+"']").prop('selected', true);
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

	$("[name=player_1A] option[value='"+players[0]+"']").prop('selected', true);
	$("[name=player_2A] option[value='"+players[1]+"']").prop('selected', true);
	if (players.length>=3) {
		if (Math.random() >= 0.5) {
			$("[name=player_1B] option[value='"+players[2]+"']").prop('selected', true);
			if (players.length==4) {
				$("[name=player_2B] option[value='"+players[3]+"']").prop('selected', true);
			}
		} else {
			$("[name=player_2B] option[value='"+players[2]+"']").prop('selected', true);
			if (players.length==4) {
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
	} else {
		if (players[3]=="") {
			// if there is no new 1A
			$("[name=player_1A] option[value='"+players[0]+"']").prop('selected', true);
			// $("[name=player_1B] option[value='"+players[0]+"']").prop('selected', true);
		} else {
			$("[name=player_1A] option[value='"+players[3]+"']").prop('selected', true);
			$("[name=player_1B] option[value='"+players[0]+"']").prop('selected', true);
		}
		if (players[1]=="") {
			$("[name=player_2A] option[value='"+players[2]+"']").prop('selected', true);
		} else {
			$("[name=player_2A] option[value='"+players[1]+"']").prop('selected', true);
			$("[name=player_2B] option[value='"+players[2]+"']").prop('selected', true);
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

	if(players.filter(Boolean).length==2) {
		$("[name=player_1A] option[value='"+players[2]+"']").prop('selected', true);
		$("[name=player_2A] option[value='"+players[0]+"']").prop('selected', true);
	} else {
		if (players[2]=="") {
			// if there is no new 1A
			$("[name=player_1A] option[value='"+players[3]+"']").prop('selected', true);
		} else {
			$("[name=player_1A] option[value='"+players[2]+"']").prop('selected', true);
			$("[name=player_1B] option[value='"+players[3]+"']").prop('selected', true);
		}
		if (players[0]=="") {
			$("[name=player_2A] option[value='"+players[1]+"']").prop('selected', true);
		} else {
			$("[name=player_2A] option[value='"+players[0]+"']").prop('selected', true);
			$("[name=player_2B] option[value='"+players[1]+"']").prop('selected', true);
		}



	}
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