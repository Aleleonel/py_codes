// Soma encadeadasde numeros de um lista

// numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
// total = 0;

// function somar(item, indice, array){
//     total += item;
//     array[indice]= total;
// }
// numeros.forEach(somar);
// console.log(numeros);

// Imprime itens de uma lista

// cores = ["Verde", "Amarelo", "Azul", "Branco"];

// function imprimir(item) {
//     console.log(item)
// }
// cores.forEach(imprimir);

// Imprime Tabuada

// numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

// function tabuadaDo2(item){
//     console.log(item*2)
// }

// numeros.forEach(tabuadaDo2);

// numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
// total = 0;
// function somar(item){
//     total += item;
// }

// numeros.forEach(somar);
// console.log(total);

// Retorna os nomes que começam com determinada letra, exemplo "F"
// marcas = ['Fiat', 'Chevrolet', 'Ford', 'Volkswagen']
// marcasIniciadaF = []
// novoIndice = 0

// function selecionaMarcas(item, indice){
//     if (marcas[indice].indexOf("F") == 0) {
//         marcasIniciadaF[novoIndice] = marcas[indice].toUpperCase();
//         novoIndice++;
//     }
// }
// marcas.forEach(selecionaMarcas);
// console.log(marcasIniciadaF);

// nomes = ['Alexandre Oliveira', 'Rosemary Aguilar', 'Leonel Oliveira', 'Aristides Aguilar'];
// maiornome = 0;
// nome = ""

// function mostraMaiorNome(item, indice){
//     if(nomes[indice].length > maiornome ){
//         nome = nomes[indice];
//         maiornome = nomes[indice].length;
        
//     }
// }

// nomes.forEach(mostraMaiorNome);
// console.log(nome);

var dados = new Array;
var media = mediaGeral = mediaDoAluno = 0

dados[0] = [ "aluno 1", 7, 8, 7, 8 ];
dados[1] = [ "aluno 2", 9, 9, 7, 7 ];
dados[2] = [ "aluno 3", 8, 8, 9, 10 ];
dados[3] = [ "aluno 4", 9, 9, 10, 6 ];

function calculaMedia(item, i){
    mediaDoAluno = ((dados[i][1] + dados[i][2] + dados[i][3]) / dados[i].length -1)
    media += mediaDoAluno;
    mediaGeral = media/dados.length;
    console.log(dados[i][0]+ " /Media: "+ mediaDoAluno.toFixed(2))
}

dados.forEach(calculaMedia);
console.log("Média Geral: "+mediaGeral.toFixed(2));