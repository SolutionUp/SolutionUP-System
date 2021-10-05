const initCpf = () => {
    const id_cpf = document.getElementById("id_cpf");

    if (id_cpf !== undefined && id_cpf !== null) {
        id_cpf.setAttribute('maxlength', 14)
        const maskOptions = {
            mask: '000.000.000-00'
        }
        const mask = IMask(id_cpf, maskOptions);
    }
}

const initCpfInList = () => {
    const maskCpf = document.getElementById('maskCpf');
    if (maskCpf !== undefined && maskCpf !== null) {
        let formatCpf = maskCpf.innerText;
        formatCpf = `${formatCpf.substring(0, 3)}.${formatCpf.substring(3, 6)}.${ formatCpf.substring(6, 9) }-${ formatCpf.substring(9, 11) }`
        maskCpf.innerText = formatCpf;
        console.log(maskCpf)
        console.log(formatCpf)
    }
}

const clearCpf = () => {
    const id_cpf = document.getElementById("id_cpf");
    id_cpf.value = id_cpf.value.replace(/([\u0300-\u036f]|[^0-9a-zA-Z\s])/g, '');
}

document.addEventListener("DOMContentLoaded", (event) => {
    initCpf();
    initCpfInList();
});

document.getElementsByTagName('form')[0].addEventListener("submit", (event) => {
    clearCpf();
});