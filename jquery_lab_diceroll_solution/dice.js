// This lab requires you to implement three different functions that create a
// die object using the three different methods:
// * simple
// * literal
// * by call_constructor

// Each object must have a property:
//   "num_faces" that is passed in as an argument by the caller
//
// and a function
//   "roll"
//
// That returns a random number between 1 and the number of faces (included)

var die;

// I chose to use the Constuctor method, so I can comment these two.
// function get_new_die_simple(num_faces) {
//   var new_dice = new Object();
//   new_dice["num_faces"] = num_faces;
//   new_dice["roll"] = roll;
//   return new_dice
// }
//
// function get_new_die_literal(num_faces) {
//   return {
//     num_faces: num_faces,
//     roll: roll
//   };
// }

function Die(num_faces) {
  this.num_faces = num_faces;
  this.roll = roll;
}

function roll() {
  return Math.floor((Math.random() * this.num_faces)) + 1
}

// Must wait until all document has been designed.
$(document).ready(function () {
  $("#status").text("Enter Number of Faces");
  // When user gives us a number of faces, we generate a new die, which we make
  // global so we can access it from everywhere in this code. Careful with global
  // variables though, they tend to pollute the memory very soon.
  $("#faces").on("change", function () {
    var num_faces = $("#faces").val();
    var num_faces_numeric = parseInt(num_faces)
    die = new Die(num_faces_numeric);
    $("#status").text("Created die with " + num_faces_numeric + " faces");
    // Now that we have a die we can show the button. Since it's only set to
    // visibiity: none, we cannote use .show(), that would act on display prop.,
    // not visibility.
    $("#roll").css('visibility','visible');
  });
  $("#roll").click(function() {
    if (die == undefined) {
      // should never be triggered. The button in this case should be hidden.
      $("#status").text("Create die first");
    } else {
      var new_value = die.roll();
      $("#status").text("Ready.");
      $("#result").text(new_value);
    }
  }); // End ready function.
});
