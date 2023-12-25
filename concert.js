$(function () {
    $(".ddl-select").each(function () {
      $(this).hide();
      var $select = $(this);
      var _id = $(this).attr("id");
      var wrapper = document.createElement("div");
      wrapper.setAttribute("class", "ddl ddl_" + _id);
  
      var input = document.createElement("input");
      input.setAttribute("type", "text");
      input.setAttribute("class", "ddl-input");
      input.setAttribute("id", "ddl_" + _id);
      input.setAttribute("readonly", "readonly");
      input.setAttribute(
        "placeholder",
        $(this)[0].options[$(this)[0].selectedIndex].innerText
      );
  
      $(this).before(wrapper);
      var $ddl = $(".ddl_" + _id);
      $ddl.append(input);
      $ddl.append("<div class='ddl-options ddl-options-" + _id + "'></div>");
      var $ddl_input = $("#ddl_" + _id);
      var $ops_list = $(".ddl-options-" + _id);
      var $ops = $(this)[0].options;
      for (var i = 0; i < $ops.length; i++) {
        $ops_list.append(
          "<div data-value='" +
            $ops[i].value +
            "'>" +
            $ops[i].innerText +
            "</div>"
        );
      }
  
      $ddl_input.click(function () {
        $ddl.toggleClass("active");
      });
      $ddl_input.blur(function () {
        $ddl.removeClass("active");
      });
      $ops_list.find("div").click(function () {
        $select.val($(this).data("value")).trigger("change");
        $ddl_input.val($(this).text());
        $ddl.removeClass("active");
      });
    });
  });
 
string =   $('#list').find(":selected").text()
split_str=string.split('$')
val = parseFloat(split_str[1]) 
number_of_seats = $('#number_of_seats').val()
total_price = val * parseInt(number_of_seats)
console.log(number_of_seats)
$('#total_price').text('$'+ (total_price.toString()))

// Set maximum value of input field
seat_type_id =   $('#list').find(":selected").val()
console.log('seat_tyoe_id',seat_type_id)
max_value_id= 'remaining_seats'+seat_type_id
console.log('max_value_id',max_value_id)
max_value = $('#remaining_seats'+seat_type_id).text()
console.log('max_value',parseInt(max_value))
$("#number_of_seats").attr({
    "max" : parseInt(max_value),        // substitute your own
});

function total_price_calculated(){

string =   $('#list').find(":selected").text()
split_str=string.split('$')
val = parseFloat(split_str[1]) 

number_of_seats = $('#number_of_seats').val()
total_price = val * parseInt(number_of_seats)

    $('#total_price').text('$'+ (total_price.toString()))


}

function add_card_number(this_el){
    value = $(this_el).val()
    console.log('card number',value)
    $('#card_number').val(value)
    console.log('card nuner 2', $('#card_number').val())
}

