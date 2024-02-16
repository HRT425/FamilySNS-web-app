let ele = document.getElementsByClassName("text");
const texts = ele[0].style.display;

document.addEventListener('DOMContentLoaded', function(){
    const mq = window.matchMedia("(min-width: 768px)" );
    function mqCheck(mq){
        if (mq.matches) {
            for (let i=0; i < ele.length; i++){
                ele[i].style.display = texts;
            }
        } else {
            for (let i=0; i < ele.length; i++){
                ele[i].style.display = "none";
            }
        }
    }
    mqCheck(mq);

    mq.addEventListener('change', mqCheck, false);
}, false);