document.addEventListener("DOMContentLoaded", function() {
  var elems = document.querySelectorAll(".dropdown-trigger");
  var instances = M.Dropdown.init(elems, {
    closeOnClick: true,
    coverTrigger: false
  });
});
console.log("fab_attached!");

// document.addEventListener("DOMContentLoaded", function() {
//   var elems = document.querySelectorAll(".fixed-action-btn");
//   var instances = M.FloatingActionButton.init(elems, {
//     direction: "top",
//     hoverEnabled: false
//   });
// });

// document.addEventListener("DOMContentLoaded", function() {
//   var elems = document.querySelectorAll(".chat");
//   var instances = M.FloatingActionButton.init(elems, {
//     direction: "left",
//     hoverEnabled: true
//   });
// });

document.addEventListener("DOMContentLoaded", function() {
  var elems = document.querySelectorAll(".chat-trigger");
  var instances = M.Dropdown.init(elems, {
    alignment: "right",
    coverTrigger: false,
    hover: true
  });
});
