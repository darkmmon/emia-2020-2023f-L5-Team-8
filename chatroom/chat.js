//onclick like
function like() 
{
  var like = document.querySelectorAll("#heart");
  var i;
  for (i = 0; i< like.length; i++) {
  like[i].style.visibility = "visible";
  }
}


function addElement() {
  var usermsg = document.getElementById("send-input").value;

  // create a new div element
  const newDiv = document.createElement("div");
  newDiv.setAttribute("class", "receiver");

  // and give it some content
  const newContent = document.createTextNode(usermsg);

  // add the text node to the newly created div
  newDiv.appendChild(newContent);

  // add the newly created element and its content into the DOM
  var currentDiv = document.getElementById("div1");
  var parentDiv = document.getElementById("chatroom");
  parentDiv.insertBefore(newDiv, currentDiv);
}

function changeTitle(newCourse) {
  var course = document.getElementById("course-name");
  newCourseName= newCourse.innerHTML;
  course.innerHTML = newCourseName
}