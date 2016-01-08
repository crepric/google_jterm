var counter_handle;

function start_count() {
  $("#start").hide(0.5);
  $("#stop").show(0.5);
  counter_handle = setInterval(increase_counter, 1000);
}

function stop_count() {
  $("#start").show(0.5);
  $("#stop").hide(0.5);
  clearInterval(counter_handle);
}

function increase_counter() {
  var current = parseInt($("#counter").text());
  // If the counter is empty, parseInt would return NaN, and we default to the
  // starting value of 0.
  if (isNaN(current)) {
    current = 0;
  }
  $("#counter").text(current+1);
}

function configure_page() {
  $("#stop").hide(0.5);
  $("#start").click(start_count);
  $("#stop").click(stop_count);
}

$(document).ready(configure_page);
