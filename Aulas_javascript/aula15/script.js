function verificar(){
    var data = new Date()
    var ano = data.getFullYear()
    var fano = document.getElementById('txtano')
    var res = document.getElementById('res')

    if (fano.value.length == 0 || Number(fano.value) > ano){
        window.alert('[erro] Verifique os dados e tente novamente!')

    }else {

        var fsex = document.getElementsByName('radsex')
        var idade = ano - Number(fano.value)
        var genero = ''
        var img = document.createElement('img')
        img.setAttribute('id', 'foto')
        if (fsex[0].checked) {
            genero = 'Homem'
            if (idade >=0 && idade < 10) {
                genero = 'menino'
                // criança
                img.setAttribute('src', 'fotos/G_bebe.png')
                res.innerHTML = `Detectamos um ${genero} com ${idade} anos.`

            }else if (idade < 21) {
                genero = 'Adolecente'
                img.setAttribute('src', 'fotos/H_jovem.png')
                res.innerHTML = `Detectamos um ${genero} com ${idade} anos.`

            }else if (idade < 60){
                genero = 'Adulto'
                img.setAttribute('src', 'fotos/H_adulto.png')
                res.innerHTML = `Detectamos um ${genero} com ${idade} anos.`

            }else {
                genero = 'Idoso'
                img.setAttribute('src', 'fotos/H_idoso.png')
                res.innerHTML = `Detectamos um ${genero} com ${idade} anos.`
            }

        }else if (fsex[1].checked) {
            genero = 'Mulher'
            if (idade >=0 && idade <= 10) {
                genro = 'menina'
                // criança
                img.setAttribute('src', 'fotos/M_bebe.png')
                res.innerHTML = `Detectamos uma ${genero} com ${idade} anos.`

            }else if (idade < 21) {
                genero = 'Adolecente'
                img.setAttribute('src', 'fotos/M_jovem.png')
                res.innerHTML = `Detectamos uma ${genero} com ${idade} anos.`

            }else if (idade < 60){
                genero = 'Mulher'
                img.setAttribute('src', 'fotos/M_adulto.png')
                res.innerHTML = `Detectamos uma ${genero} com ${idade} anos.`
            }else {
                genero = 'idosa'
                img.setAttribute('src', 'fotos/M_idoso.png')
                res.innerHTML = `Detectamos uma ${genero} com ${idade} anos.`
            }
        }
        res.style.textAlign = 'center'
        // res.innerHTML = `Detectamos ${genero} com ${idade} anos.`
        res.appendChild(img)
    }
}
