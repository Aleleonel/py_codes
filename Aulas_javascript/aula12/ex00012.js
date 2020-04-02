var agora =  new Date()
var diaSem = agora.getDay()
var hora = agora.getHours()

console.log(`Agora são exatamente ${hora}`)
// console.log(`Dia da Semna ${diaSem}`)

switch (diaSem) {
    case 0:
        console.log('Domingo')        
        break;
    
    case 1:
        console.log('Segunda-feira')
        break
    case 2:
        console.log('Terça-feira')
        break
    case 3:
        console.log('Quarta-feira')
        break
    case 4:
        console.log('Quinta-feira')
        break
    case 5:
        console.log('Sexta-feira')
        break
    case 6:
        console.log('Sabado')
        break


    default:
        break;
}

if (hora >= 0 && hora <= 12){
    console.log('Bom dia')
}else if(hora > 12 && hora <= 18){
    console.log('Boa tarde')
}else {
    console.log('Boa noite')
}