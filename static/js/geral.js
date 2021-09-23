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

// Renderiza as imagens antes de salvar
$('#id_imagem').change(function(){
    elemento = $('#id_imagem')[0]
    if (elemento.files && elemento.files[0]) {
        var src = URL.createObjectURL(elemento.files[0])
        $('#image').attr('src', src)
        $('#image').removeClass('d-none')
        $('#image_').addClass('d-none')
    }
    else{
        $('#image_').removeClass('d-none')
        $('#image').addClass('d-none')
    }
})

function resetar_imagem(){
    $("#id_imagem").val(null);
    $("#id_imagem").trigger("change")
}

// Renderiza os comprovantes antes de salvar
$('#id_comprovante').change(function(){
    elemento = $('#id_comprovante')[0]
    if (elemento.files && elemento.files[0]) {
        var src = URL.createObjectURL(elemento.files[0])
        $('#comprovante').attr('src', src)
        $('#comprovante').removeClass('d-none')
        $('#comprovante_').addClass('d-none')
    }
    else{
        $('#comprovante_').removeClass('d-none')
        $('#comprovante').addClass('d-none')
    }
})

function resetar_comprovante(){
    $("#id_comprovante").val(null);
    $("#id_comprovante").trigger("change")
}

// Exibe criação de uma nova categoria
$(".categoria-control").click(function(){
	$("#form_categoria").toggleClass('d-none d-flex');
});