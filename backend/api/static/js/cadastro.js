async function enviarFormulario(event) {
    event.preventDefault(); // Impede o recarregamento da página

    const nome = document.getElementById("nome").value;
    const senha = document.getElementById("senha").value;
    const csrs = document.querySelector("[name=csrfmiddlewaretoken]").value;

    const url = window.location.pathname;
    const id = url.substring(url.lastIndexOf("/") + 1);

    let resposta;

    if (id) {
        resposta = await apiFetch("/api/user/" + id, "PUT", {'username': nome, 'password': senha}, {'X-CSRFToken': csrs});
    } else {
        resposta = await apiFetch("/api/user/", "POST", {'username': nome, 'password': senha}, {'X-CSRFToken': csrs});
    }
    // console.log(resposta);
    if (resposta.ok) {
        window.location.href = "/home";
    } else {
        document.getElementById("mensagem").innerHTML = "Erro ao cadastrar aluno";
    }
}

document.getElementById("alunoForm").addEventListener("submit", enviarFormulario);