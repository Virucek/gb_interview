window.onload = function() {

  var loadForm = function (e) {
    var button = $(this);
    $.ajax({
      url: button.attr("data-url"),
      method: 'GET',
      beforeSend: function () {
         $("#modal-good").modal("show");
      },
      success: function (data) {
        $("#modal-good .modal-content").html(data.html_form);
      }
    });
    e.preventDefault();
  };

  var saveForm = function (e) {
    var form = $(this);
    console.log('saveform called!');
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      method: form.attr("method"),
      success: function (data) {
        if (data.form_is_valid) {
          $(".row.goods-row").html(data.html_good_list);
          $("#modal-good").modal('hide');
          console.log('save_success!');
        }
        else {
          console.log('save failure!');
          $("#modal-good .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };

  $(".js-create-good").click(loadForm);
  $("#modal-good").on("submit", ".js-good-create-form", saveForm);

};