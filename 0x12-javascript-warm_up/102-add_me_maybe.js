#!/usr/bin/node

// export addMeMaybe function
exports.addMeMaybe = function addMeMaybe (number, theFunction) {
  theFunction(number + 1);
};
