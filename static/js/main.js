$(document).ready(function() {
$('#add-text-box').click(function() {
var numTextboxes = $('#text-boxes-container').children().length;
var newTextBox = '<input type="text" name="textbox-' + numTextboxes + '"><br>';
$('#text-boxes-container').append(newTextBox);
});
});