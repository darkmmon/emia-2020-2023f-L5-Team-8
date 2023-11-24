let container=document.getElementById('chatbot-container');

let btn=document.getElementById('btn');

   let form=document.getElementById('form');

let arr1=[


 

];

const SpeechRecognition=window.SpeechRecognition || window.webkitSpeechRecognition ;

const recorder=new SpeechRecognition();

recorder.onstart=()=>{

console.log('voice is active');

 btn.innerHTML=" voice is active";

}





function botVoice(message){

 const speech= new SpeechSynthesisUtterance();


 for(let botData of arr1){

  if(message.includes(botData.name.toLowerCase())){

   speech.text=botData.text

  }

 }


 window.speechSynthesis.speak(speech);

}

recorder.onresult=(event)=>{

 console.log(event);

 const current=event.resultIndex;

  const transcript=event.results[current][0].transcript;

   container.innerHTML+=`<p class="recorder">${transcript}</p>`;

   botVoice(transcript.toLowerCase());

}

function startVoice(){

 recorder.start();

}

form.onsubmit=(e)=>{

 e.preventDefault();

    let formInput=document.getElementById('botvalue').value;

if(formInput==''){

 return false;

}

else{

container.innerHTML+=`<p class="recorder">${formInput}</p>`;

    botVoice(formInput.toLowerCase());

form.reset();

   return true;

}

}