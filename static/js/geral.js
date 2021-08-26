// Estilo para os links ativos da navbar
document.querySelectorAll('.nav-link').forEach(function(elemento){ 
    if(elemento.pathname.split('/')[1] == window.location.pathname.split('/')[1] ){
        elemento.classList.add('atual')
    }
    else{
        elemento.classList.remove('atual')
    }})

// Esconde as mensagens após um tempo
setTimeout(function() {
    document.querySelector('.messages').style.display = 'none'
}, 3000)
