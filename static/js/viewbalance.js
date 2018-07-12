$(document).ready(function() {
  $('form').submit(function(event) {
    event.preventDefault()
    form = $("form")

    $.ajax({
      'url': '/ajax/view_balance/',
      'type': 'POST',
      'data': form.serialize(),
      'dataType': 'json',
      'success': function(data) {
        alert(data['success'])
      },
    }) // END of Ajax method
    $('#id_mobile-number').val('')
    $("#id_email").val('')
    $("#id_balance").val('')
  }) // End of submit event

}) // End of document ready function