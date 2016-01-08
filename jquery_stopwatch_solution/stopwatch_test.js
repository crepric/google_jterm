QUnit.config.reorder = false;

QUnit.test(
  "Testing that increase_counter does its job",
  function( assert ) {
    // To test that increase_counter will to its job,
    // we need to see wether the text in the div with id "Counter"
    // is increased. For that we need to have such a div.
    // With Javascript, we can generate a new element and attach it.
    var counter = document.createElement('div');
    counter.id = "counter";
    document.body.appendChild(counter);
    // We pick a random value. We should also test it for special cases
    // such as "0", and an empty value as well.
    $("#counter").text("211");
    increase_counter();
    assert.equal($("#counter").text(), "212");
    // A good rule is always clean after a test, in this case we added a
    // div, we should remove it.
    document.body.removeChild(counter);
  });

QUnit.test(
  "Testing that start_count does its job",
  function( assert ) {
    // Problem: How do we test that start_count() calls the function
    // "increase counter"? We don't have control over the real function
    // from this test. We may do like we did before, add a div and check its
    // value. But that defies the purpose of unit testing, which is to test
    // each function atomically. Javascript is very flexible and lets us
    // define a new function with the same name, so that we "fake" the original
    // one. In that function we simply count how many times it was called.
    //
    // assert.async(10) means that we expect no more than 10 calls to the
    // function "done()" which async returns.
    var done = assert.async(10);
    // assert.expect(10) means that we expect EXACTLY 10 calls to assertions
    // (which are those that will happen when the new function increase_counter)
    // will be called.
    assert.expect(10);
    var count = 0;
    increase_counter = function() {
      assert.ok(true);
      // Let qunit know that we were called.
      done();
      count++;
      if (count == 10) {
        // If stop_count works fine, the test will pass.
        stop_count();
      }
    }
    // Here's the start of the test.
    start_count();
  });
