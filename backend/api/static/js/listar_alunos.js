async function deletar(id) {
    const csrs = document.querySelector("[name=csrfmiddlewaretoken]").value;
    const resposta = await apiFetch('/api/user/' + id, 'DELETE',null,{'X-CSRFToken': csrs})
    if (resposta.status == 200) {
        var linhaAluno = document.getElementById('aluno-' + id)
        linhaAluno.remove()
    }
    else {
        console.log('Erro ao deletar aluno')
    }
}
