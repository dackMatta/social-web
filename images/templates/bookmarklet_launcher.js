(function() {
    if(!window.bookmarklet){
        bookmarklet_js=document.body.appendChild(document.createElement('script'))
        bookmarklet_js.src='//127.0.0.1:8000/static/js/bookmarklet.js?r='+Math.
        floor(math.random()*999999999999999);
        window.bookmarklet=true;
    }
    else{
        bookmarklet=true;
    }
} )();