let stringVal = "i hve __to_eat my meal__ with soda_water";

let test = stringVal.replace(/(_[a-z])/g, function (match) {
  // Convert the matched group to uppercase without the underscore
  return match[1].toUpperCase();
});

console.log(test);
