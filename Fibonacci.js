function Pertence(num) {
let valor1 = 0;
let valor2 = 1;

while (valor1<=num) {
    if (valor1==num) {
        return true;
    }
    [valor1,valor2]=[valor2,valor1+valor2];
    
}
return false;
}
let numero = 19; //informe o número 

if (Pertence==numero) {
    console.log(`O número ${numero} pertence à sequência.`);
} else {
    console.log(`O número ${numero} NÃO pertence à sequência.`)
}


