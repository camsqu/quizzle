$(document).ready(function(){
  $("#q1").click(function() {
    $("#govquiz").show();
  });
  $("#q1a").click(function () {
    $("#gov1a").show();
    $("#q1a").hide();
    $("#next1").show();
  });
  $("#next1").click(function() {
    $("#next1").hide();
    $("#gov1").hide();
    $("#gov1a").hide();
    $("#gov2").show();
  });
  $("#q2a").click(function () {
    $("#gov2a").show();
    $("#q2a").hide();
    $("#next2").show();
  });
});
