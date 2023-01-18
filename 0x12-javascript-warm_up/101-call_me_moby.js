#!/usr/bin/node

// export a function
exports.callMeMoby = function callMeMoby (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
