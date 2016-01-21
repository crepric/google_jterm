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


QUnit.test(
  "Testing that for any value between 2 and 16 the number of faces is correct",
  function( assert ) {
    // Create the object using one of the three
    // function. Use a for loop to test different
    // number of faces

    // Test that num_faces is actually what
    // expected using assert.

  });


QUnit.test( "Testing that value is returned within range", function( assert ) {
    // Create a Die
    // Call roll a high number of times
    // assert that number returned is never higher than number of faces..

  });

QUnit.test( "Testing that die roll is fair", function( assert ) {

  });
