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