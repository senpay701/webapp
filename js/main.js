let tg = window.Telegram.WebApp; 

tg.expand(); 

tg.MainButton.setText(`👋 Hi, ${tg.initDataUnsafe.user.first_name} ${tg.initDataUnsafe.user.last_name}!`); 
tg.MainButton.textColor = "#FFF"; 
tg.MainButton.color = "#bc1a63"; 

let btn = document.getElementById("btn"); 

btn.addEventListener('click', function(){ 
   if (tg.MainButton.isVisible){ 
      tg.MainButton.hide() 
   }
   else{ 
      tg.MainButton.show() 
   }
});


let usercard = document.getElementById("usercard"); 

let profImg = document.createElement('img'); 
profImg.src = "image/python-icon.png"
   
let profName = document.createElement('p'); 
profName.innerText = `🆔 Ваш ID - ${tg.initDataUnsafe.user.id}\n👤 Ваше имя - ${tg.initDataUnsafe.user.first_name}\n👑 Telegram Premium - ${tg.initDataUnsafe.user.is_premium}\n🔮 Разработчик - @Your_senpay`;
   
usercard.appendChild(profImg);
usercard.appendChild(profName); 