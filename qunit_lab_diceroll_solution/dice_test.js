// This file should contain three QUnit tests, each testing objects Die created
// using EACH of the three methods described in the object.js file:
//
// * simple
// * literal
// * by call_constructor
//
// The three tests should check that:
// * The object is created and has a property num_faces and a property roll()
// * A call to roll never returns a value larger than num_faces
// * The Die is fair (i.e., the count of times each value is returned is
//   not too different, for example if roll() is called 100000 times, there should
//   not be more than 1000 difference between the value that was returned the
//   most and the value that was returned the least).

// With this helper function we create a way to call the constructor which is
// equivalent to the other two functions. In this way, all three functions
// can be tested in the same way (using the same code)
var call_constructor_method = function(num_sides){
  return new Die(num_sides);
}

// These are the names of the functions that I want to test.
var functions_to_test = ["get_new_die_simple", "get_new_die_literal", "call_constructor_method"];

QUnit.config.hidepassed = true;

QUnit.test(
  "Testing that for any value between 1 and 32 the number of faces is correct",
  function( assert ) {
    for (var i = 0; i < functions_to_test.length ; i++){
      // In function_to_test I get a string representing the name of one of
      // the functions that we want to test.
      var function_to_test = functions_to_test[i];
      for (var num_faces = 1; num_faces <= 16; num_faces++) {
        // window["function_name"]()   is equivalent to:
        // function_name().
        // JavaScript is amazing, don't you agree?
        var die = window[function_to_test](num_faces);
        assert.ok(die.num_faces != undefined, "Property exists")
        if (die.num_faces != undefined) {
          assert.equal(num_faces, die.num_faces,
                       "Checking number of faces returned by " +
                       function_to_test);
        }
      }
    }
  });


QUnit.test( "Testing that value is returned within range", function( assert ) {
    for (var i = 0; i < functions_to_test.length ; i++){
      function_to_test = functions_to_test[i];
      for (var num_faces = 1; num_faces <= 16; num_faces++) {
        var die = window[function_to_test](num_faces);
        // We need to run each number of faces a large number of times,
        // To be reasonably convinved that the behavior is randonm.
        for (var run = 1; run <= 1000; run++) {
          var my_val = die.roll();
          assert.ok(my_val <= num_faces, "checking if " + my_val + " < " +
                    num_faces + " while testing " + function_to_test);
        }
      }
    }
});

// To see if it is fair, we need to create a counter of each value, increase it
// every time we get that result, run thousands of times and then compare the
// difference between the most common and the least common results.
// We set an arbitrary acceptable_diff of 2$.
//
// This test may take a long time since it requires so many iterations. In
// real life it may be redundant, since we are using Math.random(), and that
// function has already been tested toroughly.
QUnit.test( "Testing that die roll is fair", function( assert ) {
    for (var i = 0; i < functions_to_test.length ; i++){
      function_to_test = functions_to_test[i];
      for (var num_faces = 1; num_faces <= 16; num_faces++) {
        var die = window[function_to_test](num_faces);
        var histagram = {};
        total_runs = 10000
        for (var run = 1; run <= total_runs; run++) {
          var my_val = die.roll();
          if (histagram.hasOwnProperty(my_val)) {
            histagram[my_val]++;
          } else {
            histagram[my_val] = 1;
          }
        }
        // Find max and min. There are faster ways of doing it, but this should
        // be the easiest to read and understand.
        var max_count = histagram[1];
        var min_count = histagram[1];
        for (var value = 2; value <= num_faces; value++) {
          if (histagram[value] > max_count) {
            max_count = histagram[value];
          }
          if (histagram[value] < min_count) {
            min_count = histagram[value];
          }
        }
        // Check that we get no more than 2% difference
        var acceptable_diff = total_runs * 0.02;
        assert.ok(max_count - min_count <= acceptable_diff,
                  "Histagram for num_faces: " + num_faces + " " +
                  max_count + " vs " + min_count + " while testing " +
                  function_to_test);
      }
    }
});
