function compute_tax(sum, tax_rate) {
  // This is straightforward, it's the textbook definition of how to compute tax.
  return sum * tax_rate/100;
}

function counter_checkout(prices, tax_rate, tip_percent_before_tax) {
  // So many different ways to sum all elements in an array in JavaScript:
  // Here's the most straightforward:
  var sum = 0;
  for (var i = 0; i < prices.length; i++) {
    sum += prices[i];
  }
  // Which incidentally could be shrunk in a one liner:
  //  var sum = prices.length ? 0:  for (var i = 0; i < prices.length; sum += prices[i++]);
  //
  // Or also we can use the method of JS arrays, reduce():
  // sum= prices.length ? prices.reduce(function (partial_sum, next_el) {return partial_sum + next_el;}) : 0
  //
  // ----
  // The function is called "compute_tax", but after all it is not different from
  // computing any percentage, so we can use it for tips too.
  tip_amount = compute_tax(sum, tip_percent_before_tax);
  tax_amount = compute_tax(sum, tax_rate);
  total = sum + tip_amount + tax_amount
  return total
}
