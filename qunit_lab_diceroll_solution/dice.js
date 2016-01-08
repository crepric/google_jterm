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

function get_new_die_simple(num_faces) {
  var new_dice = new Object();
  // obj["function_name"] is equivalent to obj.function_name()
  new_dice["num_faces"] = num_faces;
  new_dice["roll"] = roll;
  return new_dice
}

function get_new_die_literal(num_faces) {
  return {
    num_faces: num_faces,
    roll: roll
  };
}

function Die(num_faces) {
  this.num_faces = num_faces;
  this.roll = roll;
}

function roll() {
  return Math.floor((Math.random() * this.num_faces)) + 1
}
