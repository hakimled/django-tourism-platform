document.body.style.backgroundColor = 'lightblue';
const string = 'ledjassa hakim';
const news = string.split();
const colorEl = document.querySelector('h1');




// ledjassa abdelhakim
const btnElement = document.querySelector('button');
const divEl = document.querySelector('.model');
const colors = ['navy ', 'crimson' , 'lavender','turquoise', 
'cyan', 'indigo', 'magenta' ,'red','tomato', 'teal', 'fuchsia'];
function changColor(){
    document.addEventListener('keypress' , function(e){
        
        const randomcolor =  Math.floor(Math.random() * colors.length);
        console.log(colors[randomcolor]);
        if (e.key === ' '){
        document.body.style.backgroundColor = `${colors[randomcolor]}`;
        colorEl.innerText = `${colors[randomcolor]}`;
        colorEl.style.color = `${colors[randomcolor]}`;
        let index = colors.indexOf[colors[randomcolor]];

        }
    })

    console.log(news);
}


changColor();