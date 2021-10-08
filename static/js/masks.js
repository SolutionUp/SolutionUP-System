const maskcpf = () => {
    const id_cpf = document.getElementById("id_cpf");

    if (id_cpf !== undefined && id_cpf !== null) {
        id_cpf.setAttribute('maxlength', 14)
        const maskOptions = {
            mask: '000.000.000-00'
        }
        const mask = IMask(id_cpf, maskOptions);
    }
}

const masktelefone = () => {
    const id_telefone = document.getElementById("id_telefone");

    if (id_telefone !== undefined && id_telefone !== null) {
        id_telefone.setAttribute('maxlength', 14)
        const maskOptions = {
            mask: '(00) 0000-0000'
        }
        const mask = IMask(id_telefone, maskOptions);
    }
}

const maskcelular = () => {
    const id_celular = document.getElementById("id_celular");

    if (id_celular !== undefined && id_celular !== null) {
        id_celular.setAttribute('maxlength', 15)
        const maskOptions = {
            mask: '(00) 00000-0000'
        }
        const mask = IMask(id_celular, maskOptions);
    }
}

const cleancpf = () => {
    const id_cpf = document.getElementById("id_cpf");
    id_cpf.value = id_cpf.value.replace(/([\u0300-\u036f]|[^0-9a-zA-Z\s])/g, '');
}

const cleantelefone = () => {
    const id_telefone = document.getElementById("id_telefone");
    id_telefone.value = id_telefone.value.replace(/(?<!^)\+|[^\d+]+/g, '');
}

const cleancelular = () => {
    const id_celular = document.getElementById("id_celular");
    id_celular.value = id_celular.value.replace(/(?<!^)\+|[^\d+]+/g, '');
}

document.addEventListener("DOMContentLoaded", (event) => {
    maskcpf();
    masktelefone();
    maskcelular();
});

document.getElementsByTagName('form')[0].addEventListener("submit", (event) => {
    cleancpf();
});

document.getElementsByTagName('form')[0].addEventListener("submit", (event) => {
    cleantelefone();
});

document.getElementsByTagName('form')[0].addEventListener("submit", (event) => {
    cleancelular();
});

document.getElementsByTagName('form')[1].addEventListener("submit", (event) => {
    cleancpf();
});