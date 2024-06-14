import Tostify from 'toastify-js'
import "toastify-js/src/toastify.css"

export default function showMessage(message,state='error',callback_func){
    let background_color;
    if(state==='error'){
        background_color = 'linear-gradient(to right, #ff5f6d,#ffc371)'
    }else{
        background_color='linear-gradient(to right, #00b09b,#96c93d)'
    }
    Tostify(
    {
        text:message,
        duration:2000,
        close:true,
        gravity:'top',
        position:'center',
        stopOnFocus:true,
        style:{
            background:background_color,
        },
        callback:function(){
            if(!callback_func) return;
            if(callback_func){
                callback_func()
            }
        },
        onClick:function(){}
    }
    ).showToast();
}